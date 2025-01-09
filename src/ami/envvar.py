import os


def envvar_is_set(var: str) -> bool:
    """
    Check if an environment variable is set.

    Args:
        var (str): Name of the environment variable to check

    Returns:
        bool: True if the environment variable exists, False otherwise
    """
    return var in os.environ


def using_envvar(var: str, value: str | None = None) -> bool:
    """
    Check if an environment variable is set and optionally matches a specific value.

    Args:
        var (str): Name of the environment variable to check
        value (str, optional): Value to compare against. Defaults to None.

    Returns:
        bool: True if the environment variable exists and matches value (if provided),
              False otherwise
    """

    if var not in os.environ:
        return False

    if value is not None:
        return os.environ[var] == value

    return True
