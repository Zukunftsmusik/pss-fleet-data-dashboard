from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException


app = FastAPI(title="PSS Fleet Data Dashboard - Gateway Testing")


origins = [
    "http://localhost:5173",  # Vite local development server port
    "http://127.0.0.1:5173",  # Alternative local loopback port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests coming from your local Vite server
    allow_credentials=True,  # Allows authorization cookies or tokens to pass through
    allow_methods=["*"],  # Allows standard actions (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Allows custom layout or authentication headers
)


# ==========================================
# 1. API Endpoints (For testing CapRover Nginx routing)
# ==========================================
@app.get("/api/v1/test")
async def test_api_route():
    """Use this to verify that CapRover securely forwards /api traffic."""
    return {
        "status": "online",
        "message": "Greetings from the backend! Nginx routing is working perfectly.",
        "container_environment": "CapRover Production Stack",
    }


# ==========================================
# 2. Hardcoded 90s Landing Page & SPA Fallback
# ==========================================
FRONTEND_DIST_DIR = Path("/app/frontend/dist")

if FRONTEND_DIST_DIR.exists():
    # Mount to the bare '/' root context path internally inside the container,
    # so paths like /dashboard/assets look exactly like /assets to the static disk finder!
    app.mount("/", StaticFiles(directory=FRONTEND_DIST_DIR, html=True), name="frontend")

    # Clean catch-all fallback handler for Vue Router (SPA history mode support)
    @app.exception_handler(StarletteHTTPException)
    async def spa_page_fallback(request, exc):
        if exc.status_code == 404:
            # If a user reloads the page or accesses a frontend path, send the base index.html
            return FileResponse(FRONTEND_DIST_DIR / "index.html")
        raise exc


# HTML Template for the glorious 90s Under Construction theme
GLORIOUS_90S_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>⚡ PSS FLEET DATA DASHBOARD - UNDER CONSTRUCTION ⚡</title>
    <style>
        body {
            background-color: #000080; /* Classic Windows Blue */
            color: #00FF00;           /* Terminal Green Text */
            font-family: "MS Sans Serif", "Courier New", monospace;
            text-align: center;
            padding: 50px;
        }
        h1 {
            color: #FFCC00;
            font-size: 3em;
            text-shadow: 3px 3px #FF0000;
            margin-bottom: 10px;
        }
        marquee {
            background-color: #FF0000;
            color: #FFFFFF;
            font-weight: bold;
            padding: 5px;
            font-size: 1.2em;
            border: 3px outset #FFF;
            margin: 20px 0;
        }
        .gif-container {
            margin: 30px auto;
            max-width: 300px;
            border: 4px ridge #808080;
            background: #C0C0C0;
            padding: 10px;
        }
        .visitor-counter {
            font-size: 1.5em;
            color: #FFFFFF;
            background: #000000;
            border: 2px inset #808080;
            display: inline-block;
            padding: 5px 15px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>⚠️ PSS FLEET DATA ⚠️</h1>
    <h2>*** DASHBOARD SYSTEM IS UNDER CONSTRUCTION ***</h2>

    <marquee scrollamount="10">⚡⚡ WELCOME TO THE FUTURE -- LAUNCHING SOON -- STAY TUNED ⚡⚡</marquee>

    <!-- The requested classic Tenor construction GIF -->
    <div class="gif-container">
        <div class="tenor-gif-embed" data-postid="7848558" data-share-method="host" data-aspect-ratio="0.876494" data-width="100%">
            <a href="https://tenor.com/view/under-construction-men-at-work-gif-7848558">Under Construction Men At Work GIF</a>
        </div> 
        <script type="text/javascript" async src="https://tenor.com/embed.js"></script>
    </div>

    <p>Webmaster Contact: <a href="mailto:theworstpss@gmail.com" style="color: #00FFFF;">theworstpss@gmail.com</a></p>

    <div class="visitor-counter">
        VISITOR COUNT: 000001
    </div>

</body>
</html>
"""
