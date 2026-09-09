from app.models.exceptions import (
    PlayerNotFoundError,
)


def player_not_found(search_string: str) -> PlayerNotFoundError:
    """Creates a `PlayerNotFoundError` based on the given parameters.

    Args:
        search_string (str): The string used to search for the Player.

    Returns:
        PlayerNotFoundError: An exception to be raised.
    """
    return PlayerNotFoundError(
        details=f"There is currently no Player with the name '{search_string}'.",
        suggestion="Check the provided `collectionId` and `playerId` parameters in the path.",
    )


__all__ = [
    "player_not_found",
]
