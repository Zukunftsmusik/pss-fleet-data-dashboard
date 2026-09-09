import datetime
from typing import cast

import dateutil

from .config import CONSTANTS
from .models.enums import UserAllianceMembership, UserAllianceMembershipEncoded


ALLIANCE_MEMBERSHIP_ENCODE_LOOKUP = {
    UserAllianceMembership.NONE: UserAllianceMembershipEncoded.NONE,
    UserAllianceMembership.CANDIDATE: UserAllianceMembershipEncoded.CANDIDATE,
    UserAllianceMembership.ENSIGN: UserAllianceMembershipEncoded.ENSIGN,
    UserAllianceMembership.LIEUTENANT: UserAllianceMembershipEncoded.LIEUTENANT,
    UserAllianceMembership.MAJOR: UserAllianceMembershipEncoded.MAJOR,
    UserAllianceMembership.COMMANDER: UserAllianceMembershipEncoded.COMMANDER,
    UserAllianceMembership.VICE_ADMIRAL: UserAllianceMembershipEncoded.VICE_ADMIRAL,
    UserAllianceMembership.FLEET_ADMIRAL: UserAllianceMembershipEncoded.FLEET_ADMIRAL,
}


ALLIANCE_MEMBERSHIP_DECODE_LOOKUP = {value: key for key, value in ALLIANCE_MEMBERSHIP_ENCODE_LOOKUP.items()}


def add_timezone_utc(dt: datetime.datetime | None) -> datetime.datetime | None:
    """Takes a `datetime` and makes it a timezone-aware `datetime` with timezone UTC, if it's not timezone-aware, yet.

    Args:
        dt (datetime.datetime | None): The `datetime` to be localized to the UTC timezone.

    Raises:
        ValueError: Raised, if parameter `dt` is not of type `datetime.datetime`.

    Returns:
        datetime.datetime | None: The timezone-aware `datetime.datetime` with the UTC timezone, if the provided `datetime.datetime` is not timezone-aware. The provided timezone-aware `datetime.datetime`, if it's not `None`. `None`, else.
    """
    if dt is None:
        return None

    if not isinstance(dt, datetime.datetime):
        raise TypeError("The parameter `dt` must be of type `datetime.datetime`!")

    if not dt.tzinfo:
        return dt.replace(tzinfo=datetime.UTC)
    else:
        return dt


def convert_datetime_to_seconds(dt: datetime.datetime | None) -> int | None:
    """Takes a `datetime` and converts it to seconds since the PSS start date.

    Args:
        dt (datetime.datetime | None): The `datetime.datetime` to be localized to the UTC timezone.

    Raises:
        TypeError: Raised, if parameter `dt` is not of type `datetime.datetime`.

    Returns:
        int | None: The seconds since the PSS start date. 0, if the provided `datetime.datetime` is before the PSS start date. `None`, else.
    """
    if dt is None:
        return None

    if not isinstance(dt, datetime.datetime):
        raise TypeError("The parameter `dt` must be of type `datetime.datetime`!")

    dt = cast(datetime.datetime, localize_to_utc(dt))
    if dt < CONSTANTS.pss_start_date:
        return 0

    return int((dt - CONSTANTS.pss_start_date).total_seconds())


def decode_alliance_membership(membership: int | UserAllianceMembershipEncoded) -> UserAllianceMembership:
    """Converts an `int` or `UserCreateAllianceMembership` enum into a `UserAllianceMembership`.

    Args:
        membership (int | UserAllianceMembershipEncoded): The alliance membership (member rank) to be decoded.

    Raises:
        ValueError: Raised, if parameter `membership` is `None` or not a valid value for the enum `UserCreateAllianceMembership`.
        TypeError: Raised, if parameter `membership` is not of type `int` or `UserCreateAllianceMembership`.

    Returns:
        UserAllianceMembership: The decoded alliance membership (member rank).
    """
    if membership is None:
        raise ValueError("The parameter `membership` must not be `None`!")

    if isinstance(membership, bool) or not isinstance(membership, (int, UserAllianceMembershipEncoded)):
        raise TypeError("The parameter `membership` must be of type `int` or `UserCreateAllianceMembership`!")

    if isinstance(membership, int):
        membership = UserAllianceMembershipEncoded(membership)

    return ALLIANCE_MEMBERSHIP_DECODE_LOOKUP.get(membership, UserAllianceMembership.NONE)


def encode_alliance_membership(membership: str | UserAllianceMembership) -> int:
    """Converts a `str` or `UserAllianceMembership` enum into an `int`.

    Args:
        membership (str | UserAllianceMembership]): The alliance membership (member rank) to be encoded.

    Raises:
        TypeError: Raised, if the parameter `membership` is not of type `str` or `UserAllianceMembership`.
        ValueError: Raised, if the parameter `membership` is `None` or not a valid value of the `StrEnum` `UserAllianceMembership`.

    Returns:
        int: An `int` representing an encoded `AllianceMembership` value.
    """
    if not membership:
        raise ValueError("Parameter `membership` must not be `None`!")

    if not isinstance(membership, (str, UserAllianceMembership)):
        raise TypeError("Parameter `membership` must be of type `str` or `UserAllianceMembership`!")

    if isinstance(membership, str):
        membership = UserAllianceMembership(membership)

    return int(ALLIANCE_MEMBERSHIP_ENCODE_LOOKUP.get(membership, UserAllianceMembershipEncoded.NONE))


def localize_to_utc(dt: datetime.datetime | None) -> datetime.datetime | None:
    """Takes a `datetime` and converts it to a timezone-aware UTC `datetime`.

    Args:
        dt (datetime.datetime | None): The `datetime.datetime` to be localized to the UTC timezone.

    Raises:
        ValueError: Raised, if parameter `dt` is not of type `datetime.datetime`.

    Returns:
        datetime.datetime | None: The localized `datetime.datetime`, if `dt` is not `None`. `None`, else.
    """
    if dt is None:
        return None

    if not isinstance(dt, datetime.datetime):
        raise TypeError("The parameter `dt` must be of type `datetime.datetime`!")

    if not dt.tzinfo:
        return add_timezone_utc(dt)
    elif dt.tzinfo != datetime.UTC:
        return dt.astimezone(datetime.UTC)
    else:
        return dt


def parse_datetime(dt: datetime.datetime | int | str | None) -> datetime.datetime | None:
    """Parses a `str` or `int` to `datetime.datetime` or returns the passed datetime.

    Args:
        dt (datetime.datetime | int | str | None): The `str` or `int` to be parsed. If it's an `int`, it represents the seconds since Jan 6th, 2016 12 am.

    Raises:
        ValueError: Raised, if parameter `dt` is not of type `datetime.datetime`, `int` or `str`.

    Returns:
        datetime.datetime | None: The parsed `datetime.datetime`, if `dt` is not `None`. `None`, else.
    """
    if dt is None:
        return None

    if not isinstance(dt, (datetime.datetime, int, str)) or isinstance(dt, bool):
        raise TypeError("The parameter `dt` must be of type `datetime.datetime`, `int` or `str`!")

    if isinstance(dt, int):
        # If it's an integer value, then it's likely encoded as seconds from Jan 6th, 2016 00:00 UTC
        return CONSTANTS.pss_start_date + datetime.timedelta(seconds=dt)
    elif isinstance(dt, str):
        if not dt:
            return None
        return dateutil.parser.parse(dt)
    return dt


def remove_timezone(dt: datetime.datetime | None) -> datetime.datetime | None:
    """Removes timezone information from a timezone-aware `datetime` object.

    Args:
        dt (datetime.datetime | None): The `datetime.datetime` to remove the timezone information from.

    Raises:
        TypeError: Raised, if parameter `dt` is not of type `datetime.datetime`.

    Returns:
        datetime.datetime | None: A timezone-naive `datetime.datetime` object.
    """
    if dt is None:
        return None

    if not isinstance(dt, datetime.datetime):
        raise TypeError("The parameter `dt` must be of type `datetime.datetime`!")

    return dt.replace(tzinfo=None)
