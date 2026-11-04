# CarService

Responsive Georgian / English / Russian tow-truck request website with light and dark themes.

Serve this directory with any static HTTPS host (Vercel or GitHub Pages). No build step or backend is required. Local preview: `python -m http.server 8000`.

## Request flow

The visitor explicitly adds a one-time GPS position or enters an address, describes the problem, and opens WhatsApp with the prepared request. The visitor must press Send in WhatsApp. Viber and Messenger buttons copy the request and open the configured chat; the visitor pastes and sends it. A manual-copy fallback is provided when clipboard permission is unavailable. There is no automatic dispatch, delivery confirmation, continuous tracking, or stored order database. Availability, price and arrival time are agreed directly with the operator.

Contact configuration: `CONTACT` in `app.js` and contact links in `index.html`. Main phone: +995591622929. WhatsApp/Viber: +995592078078. Social profiles: @miqelius88. Verify account ownership and installed-app deep links on the target phones before handing off to another operator.

The unauthenticated legacy WebSocket prototype and its client-side-PIN driver panel were removed from this branch for customer privacy. A previously deployed Render backend, if any, must also be disabled or replaced independently: deleting repository files does not automatically shut down deployed services.

## Visuals

The site uses locally hosted illustrative stock photographs from Pexels, not photos of the operator's fleet. See `assets/PHOTO-CREDITS.md` for sources. The former AI-generated `tow-hero.webp` is retained but is no longer used by the page.

## Sober driver and tours

Sober-driver requests require a destination and use the customer's own vehicle. Georgia tour requests require an itinerary, a current/future departure date and passenger count, plus sedan/minivan/SUV preference. All fields are included in the messenger request. Vehicle capacity, luggage, availability and price are confirmed by the operator; no booking is automatically accepted.

## Release notes — customer-ready refresh

- More compact responsive hero, readable service tiles and accessible focus styling.
- Better mobile form layout and larger touch targets; preserved three-language text, map/GPS, and messenger handoff.
- Updated live location preview immediately when typing an address.
- WhatsApp handoff has a same-tab fallback when a popup is blocked.
- Removed unsafe legacy live-location prototype from the source tree. This site remains a static, inquiry-only demo, not a dispatch platform.

Before selling or deploying for another operator, verify phone numbers, social handles, address, licensed photographs, and the WhatsApp/Viber deep-link behavior on physical phones.
