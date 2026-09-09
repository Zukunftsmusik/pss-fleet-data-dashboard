from dataclasses import dataclass
from datetime import UTC, datetime
from os import getenv
from typing import ClassVar


@dataclass(frozen=True)
class Constants:
    """
    A collection of application-wide constants.
    """

    latest_schema_version: int = 9
    pss_start_date: datetime = datetime(2016, 1, 6, tzinfo=UTC)


@dataclass(frozen=True)
class Settings:
    """
    A collection of application settings.
    """

    # Base
    project_name: str = "PSS Fleet Data API"
    version: str = "1.6.1"
    description: str = "An API server for Pixel Starships Fleet Data."
    contact: ClassVar[dict[str, str]] = {
        "email": "theworstpss@gmail.com",
        "name": "The worst.",
        "url": "https://fleetdata.dolores2.xyz/dashboard/api",
    }
    license: ClassVar[dict[str, str]] = {
        "name": "MIT",
        "url": "https://github.com/Zukunftsmusik/pss-fleet-data-dashboard/blob/main/LICENSE",
    }
    servers: ClassVar[list[dict[str, str | dict | set]]] = [
        {
            "url": getenv("FLEET_DATA_DASHBOARD_API_URL_OVERRIDE", "https://fleetdata.dolores2.xyz/dashboard/api"),
            "description": getenv("FLEET_DATA_DASHBOARD_API_URL_DESCRIPTION_OVERRIDE", "The original PSS Fleet Data Dashboard API."),
            "variables": {},
        },
    ]
    discord_client_id: str | None = getenv("FLEET_DATA_DASHBOARD_DISCORD_CLIENT_ID")
    discord_client_secret: str | None = getenv("FLEET_DATA_DASHBOARD_DISCORD_CLIENT_SECRET")
    dashboard_session_secret: str | None = getenv("FLEET_DATA_DASHBOARD_SESSION_SECRET")
    fleet_data_api_base_url: str = getenv("FLEET_DATA_API_BASE_URL", "https://fleetdata.dolores2.xyz")
    pssapi_public_access_token: str = getenv("PSSAPI_PUBLIC_ACCESS_TOKEN", "")

    # Database
    database_engine_echo: bool = getenv("DATABASE_ENGINE_ECHO", "false") == "true"
    async_database_connection_str: str = f"postgresql+asyncpg://{getenv('DATABASE_URL')}/{getenv('DATABASE_NAME', 'pss-fleet-data-dashboard')}"
    sync_database_connection_str: str = f"postgresql://{getenv('DATABASE_URL')}/{getenv('DATABASE_NAME', 'pss-fleet-data-dashboard')}"

    # Flags
    create_dummy_data_on_startup: bool = getenv("CREATE_DUMMY_DATA", "false") == "true"
    debug: bool = getenv("DEBUG_MODE", "false") == "true"
    in_github_actions: bool = getenv("GITHUB_ACTIONS", "false") == "true"  # True if in github actions
    reinitialize_database_on_startup: bool = getenv("REINITIALIZE_DATABASE", "false") == "true"

    # Access
    root_api_key: str | None = getenv("ROOT_API_KEY", None)


SETTINGS = Settings()
CONSTANTS = Constants()

if not SETTINGS.pssapi_public_access_token:
    raise ValueError("The environment variable 'PSSAPI_PUBLIC_ACCESS_TOKEN' must be set to a valid PSSAPI public access token.")


__all__ = [
    # Variables
    "CONSTANTS",
    "SETTINGS",
    # Classes
    "Constants",
    "Settings",
]
