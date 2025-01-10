"""
Module for detecting Quarto publishing system environments.
"""

from .envvar import using_envvar


def using_quarto() -> bool:
    """
    Check if running in a Quarto environment.

    Returns:
        bool: True if Quarto is available, False otherwise.
    """
    quarto_vars = {
        "QUARTO_DOCUMENT_PATH",
        "QUARTO_PROJECT_ROOT",
        "QUARTO_PROFILE",
        "QUARTO_FIG_WIDTH",
        "QUARTO_FIG_HEIGHT",
        "QUARTO_RUN_NO_NETWORK",
    }
    return any(using_envvar(var) for var in quarto_vars)
