"""
Module for Conda environment detection and functionality.
"""

from .envvar import using_envvar


def using_conda(env: str | None = None) -> bool:
    """
    Check if currently running in a Conda environment.

    Args:
        env: Optional name of the Conda environment to check for.
             If provided, returns True only if running in that specific environment.
             If None, returns True for any Conda environment.

    Returns:
        bool: True if running in a matching Conda environment, False otherwise.
    """

    return using_envvar("CONDA_DEFAULT_ENV", env)
