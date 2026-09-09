from app.models.enums import OperationId
from app.models.link import LinkDefinition


# /players


players_getPlayerHistory = LinkDefinition(
    description="A `playerId` value in the response can be used as the `playerId` parameter in `GET /players/{playerId}`.",
    operationId=OperationId.GET_PLAYER_HISTORY,
    parameters={
        "playerId": "$response.body#/0/player_id",
    },
)


__all__ = [
    "players_getPlayerHistory",
]
