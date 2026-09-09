from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException

from . import routers


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

app.include_router(routers.v1, prefix="/dashboard/api")


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
