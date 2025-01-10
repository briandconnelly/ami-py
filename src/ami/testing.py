"""
Module for detecting testing frameworks.
"""

from .envvar import using_envvar


def using_pytest() -> bool:
    """
    Check if running under pytest.

    Returns:
        bool: True if running under pytest, False otherwise.
    """
    return using_envvar("PYTEST_CURRENT_TEST")


def using_tox() -> bool:
    """
    Check if running under tox.

    Returns:
        bool: True if running under tox, False otherwise.
    """
    return using_envvar("TOX_ENV_NAME")
