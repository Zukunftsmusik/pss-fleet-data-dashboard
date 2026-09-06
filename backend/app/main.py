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
    dashboard_app = FastAPI(title="Vue Dashboard Host")

    # FIX: Intercept the blank sub-app root route and deliver index.html directly!
    @dashboard_app.get("/", response_class=FileResponse)
    async def serve_dashboard_index():
        return FileResponse(FRONTEND_DIST_DIR / "index.html")

    # Mount static assets directory context behind an explicit sub-route flag
    # This prevents the asset compilation chunks from clashing with the root loader path
    dashboard_app.mount("/", StaticFiles(directory=FRONTEND_DIST_DIR, html=True), name="static")

    # Handle structural catch-all fallback routines for SPA sub-view history routing
    @dashboard_app.exception_handler(StarletteHTTPException)
    async def spa_fallback(request, exc):
        if exc.status_code == 404:
            return FileResponse(FRONTEND_DIST_DIR / "index.html")
        return exc

    # Securely map the sub-application infrastructure down under the core prefix string
    app.mount("/dashboard", dashboard_app)


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
