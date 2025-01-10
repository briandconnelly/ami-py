"""
Module for detecting Positron IDE environments.
"""

from typing import Literal, Union

from .envvar import using_envvar


def using_positron(mode: Union[Literal["desktop"], Literal["server"], None] = None) -> bool:  # noqa: E501
    """
    Check if running in Positron IDE.

    Args:
        mode: Optional mode to check for.
              If 'desktop', checks specifically for desktop IDE.
              If 'server', checks specifically for server IDE.
              If None, checks for any Positron IDE mode.

    Returns:
        bool: True if running in Positron IDE (in specified mode if given),
              False otherwise.
    """
    return using_envvar("POSITRON_MODE", mode)


def using_positron_desktop() -> bool:
    """
    Check if running in Positron Desktop IDE.

    Returns:
        bool: True if running in Positron Desktop IDE, False otherwise.
    """
    return using_positron("desktop")


def using_positron_server() -> bool:
    """
    Check if running in Positron Server IDE.

    Returns:
        bool: True if running in Positron Server IDE, False otherwise.
    """
    return using_positron("server")
