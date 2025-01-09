from .envvar import using_envvar


def using_virtualenv(env: str | None = None) -> bool:
    """
    Check if a Python virtual environment is active.

    Args:
        env (str, optional): Name of the virtual environment. Defaults to None.

    Returns:
        bool: True if VIRTUAL_ENV environment variable matches the specified env
              or is set (when env is None), False otherwise
    """
    return using_envvar("VIRTUAL_ENV", env)
