from fastapi import status

from app.models.endpoint import EndpointDefinition
from app.models.enums import OperationId

from . import links, responses


players_get = EndpointDefinition(
    summary="Search a players.",
    description="Search for players by name. The search string can be a full or partial name, and the search is case-insensitive.",
    operation_id=OperationId.GET_SEARCH_PLAYERS,
    status_code=status.HTTP_200_OK,
    response_description="A list of objects denoting players with names matching the search string.",
    responses={
        **responses.get_default_responses_for_get(
            include_204=False,
            include_404=True,
            description_404="A player with this name could not be found.",
        ),
        status.HTTP_200_OK: {
            "description": "A list of objects denoting players with names matching the search string.",
            "links": {
                OperationId.GET_PLAYER_HISTORY: links.players_getPlayerHistory,
            },
        },
    },
)

players_playerId_get = EndpointDefinition(
    summary="Get a player's history.",
    description="Get the complete history or a subset of the history of a specific player and current player data. You can use the parameters to limit the result set.",
    operation_id=OperationId.GET_PLAYER_HISTORY,
    status_code=status.HTTP_200_OK,
    response_description="All relevant historic and current data for the requested player.",
    responses={
        **responses.get_default_responses_for_get(
            include_204=True,
            include_404=True,
            description_404="The requested player could not be found.",
        ),
        status.HTTP_200_OK: {
            "description": "All relevant historic and current data for the requested player.",
            "links": {},
        },
    },
)


__all__ = [
    "players_get",
    "players_playerId_get",
]
