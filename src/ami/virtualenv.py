from pathlib import Path

from .envvar import using_envvar


def using_virtualenv(path: Path |str | None = None) -> bool:
    """
    Check if a Python virtual environment is active.

    Args:
        path (str, optional): Path of the virtual environment. Defaults to None.

    Returns:
        bool: True if VIRTUAL_ENV environment variable matches the specified path
              or is set (when env is None), False otherwise
    """
    if path is not None:
        path = str(path)
    return using_envvar("VIRTUAL_ENV", path)
