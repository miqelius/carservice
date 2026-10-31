# CarService

Responsive Georgian / English / Russian tow-truck request website with light and dark themes.

Serve this directory with any static HTTPS host (Vercel or GitHub Pages). No build step or backend is required. Local preview: `python -m http.server 8000`.

## Request flow

The visitor explicitly adds a one-time GPS position or enters an address, describes the problem, and opens WhatsApp with the prepared request. The visitor must press Send in WhatsApp. Viber and Messenger buttons copy the request and open the configured chat; the visitor pastes and sends it. A manual-copy fallback is provided when clipboard permission is unavailable. There is no automatic dispatch, delivery confirmation, continuous tracking, or stored order database. Availability, price and arrival time are agreed directly with the operator.

Contact configuration: `CONTACT` in `app.js` and contact links in `index.html`. Main phone: +995591622929. WhatsApp/Viber: +995592078078. Social profiles: @miqelius88. Verify account ownership and installed-app deep links on the target phones before handing off to another operator.

`main.py` and `driver-panel-secure-777.html` are legacy live-location prototype files, unused by the static site. Do not use that prototype for customer location data: its broadcast channel has no authentication or recipient isolation.

## Visual

`assets/tow-hero.webp` is an AI-generated illustrative marketing image, not a photograph of an operator's actual fleet. Created with the built-in image generation tool. Prompt: modern yellow flatbed recovery truck carrying a secured graphite sedan, safe roadside turnout near Tbilisi and Caucasus foothills, blue hour and amber lights, cinematic wide photograph, negative space at left, no text or logos.

## Sober driver and tours

Sober-driver requests require a destination and use the customer's own vehicle. Georgia tour requests require an itinerary, a current/future departure date and passenger count, plus sedan/minivan/SUV preference. All fields are included in the messenger request. Vehicle capacity, luggage, availability and price are confirmed by the operator; no booking is automatically accepted.
