"""
Module for detecting uv environments.
"""

from .envvar import using_envvar


def using_uv() -> bool:
    """
    Check if running in a uv package or project environment

    Returns:
        bool: True if running in uv, False otherwise.
    """
    return using_envvar("UV")
