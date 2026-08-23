import os
import json
import uuid
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
import redis.asyncio as redis

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Redis-ის კავშირი (ავტომატურად იღებს გარემოს ცვლადს ან მუშაობს ლოკალურად)
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
redis_client = redis.from_url(REDIS_URL, decode_responses=True)

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, list[WebSocket]] = {}

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        if session_id not in self.active_connections:
            self.active_connections[session_id] = []
        self.active_connections[session_id].append(websocket)

    def disconnect(self, session_id: str, websocket: WebSocket):
        if session_id in self.active_connections:
            if websocket in self.active_connections[session_id]:
                self.active_connections[session_id].remove(websocket)
            if not self.active_connections[session_id]:
                del self.active_connections[session_id]

    async def broadcast(self, session_id: str, message: str):
        if session_id in self.active_connections:
            for connection in list(self.active_connections[session_id]):
                try:
                    await connection.send_text(message)
                except:
                    self.disconnect(session_id, connection)

manager = ConnectionManager()

# სერვერის გამოღვიძებისთვის (Health check)
@app.get("/health")
async def health_check():
    return {"status": "awake"}

# უნიკალური სესიის შექმნა აკაუნტის გარეშე
@app.post("/api/create-order")
async def create_order():
    session_id = str(uuid.uuid4())[:8]
    # საწყისი წერტილი Redis-ში
    await redis_client.set(f"session:{session_id}", json.dumps({"lat": 41.7151, "lng": 44.8271}))
    return {"session_id": session_id}

# WebSocket რეალური დროის კოორდინატებისთვის
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(session_id, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            
            # Ping-Pong კავშირის შესანარჩუნებლად
            if message_data.get("type") == "ping":
                await websocket.send_text(json.dumps({"type": "pong"}))
                continue

            # ვინახავთ Redis-ში და ვავრცელებთ
            await redis_client.set(f"session:{session_id}", data)
            await manager.broadcast(session_id, data)
            
    except WebSocketDisconnect:
        manager.disconnect(session_id, websocket)