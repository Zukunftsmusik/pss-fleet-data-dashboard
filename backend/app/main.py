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

api_app = FastAPI(title="PSS Fleet Data Dashboard API", redirect_slashes=True)
api_app.include_router(routers.v1)
app.mount("/dashboard/api", api_app)


# ==========================================
# 2. Static Dashboard Homepage
# ==========================================
FRONTEND_DIST_DIR = Path(__file__).resolve().parents[2] / "frontend" / "dist"

if FRONTEND_DIST_DIR.exists():
    dashboard_app = FastAPI(title="Vue Dashboard Host")

    @dashboard_app.exception_handler(StarletteHTTPException)
    async def frontend_fallback(request, exc):
        if exc.status_code == 404:
            return FileResponse(FRONTEND_DIST_DIR / "index.html")
        return exc

    dashboard_app.mount(
        "/",
        StaticFiles(directory=FRONTEND_DIST_DIR, html=True),
        name="static",
    )
    app.mount("/dashboard", dashboard_app)
