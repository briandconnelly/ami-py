from .envvar import using_envvar


def using_vscode() -> bool:
    """Determine whether Visual Studio Code (or a derivative) is being used

    Returns:
        bool: True if Visual Studio Code (or a derivative) is being used and False
              otherwise
    """
    return using_envvar("TERM_PROGRAM", "vscode")
