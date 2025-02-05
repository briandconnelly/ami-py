"""
Module for detecting GitHub environments.
"""

from .envvar import using_envvar


def using_github_actions() -> bool:
    """
    Check if running in GitHub Actions.

    Returns:
        bool: True if running in GitHub Actions, False otherwise.
    """
    return using_envvar("GITHUB_ACTIONS")


def using_github_codespaces(name: str | None = None) -> bool:
    """
    Check if running in GitHub Codespaces.

    Args:
        name (str, optional): Name of a Codespace to check for. Defaults to None.

    Returns:
        bool: True if running in GitHub Codespaces (and in the specified
              Codespace if name is provided), False otherwise.
    """
    if not using_envvar("CODESPACES", "true"):
        return False

    return using_envvar("CODESPACE_NAME", name)
