"""
Module for detecting UV environments.
"""

from .envvar import using_envvar


def using_uv() -> bool:
    """
    Check if running in a UV package or project.

    Returns:
        bool: True if running in UV, False otherwise.
    """
    return using_envvar("UV")
