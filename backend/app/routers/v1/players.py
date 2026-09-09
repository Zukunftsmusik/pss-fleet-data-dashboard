from typing import Annotated

import pss_fleet_data
import pssapi
from fastapi import APIRouter, Path, Query

from app import config

from . import endpoints, exceptions


router = APIRouter(prefix="/players", tags=["players"])


@router.get("/", **endpoints.players_get)
async def search_player(search_string: Annotated[str, Query(..., description="String to be searched in player names")]):
    pss_client = pssapi.PssApiClient()
    players = await pss_client.user_service.search_users(search_string)

    if not players:
        raise exceptions.player_not_found(search_string)

    return players


@router.get("/{player_id}", **endpoints.players_playerId_get)
async def get_player_history(player_id: Annotated[int, Path(..., description="ID of the player to retrieve history for")]):
    pss_client = pssapi.PssApiClient()
    current_player_data = None
    try:
        current_player_data = await pss_client.alliance_service.get_user(config.SETTINGS.pssapi_public_access_token, player_id)
    except pssapi.utils.exceptions.PssApiError:
        pass

    fleet_data_client = pss_fleet_data.PssFleetDataClient(config.SETTINGS.fleet_data_api_base_url)
    player_history = None
    try:
        player_history = await fleet_data_client.get_user_history(player_id)
    except pss_fleet_data.exceptions.ApiError:
        pass

    return {"current": current_player_data, "history": player_history}


__all__ = [
    "router",
]
