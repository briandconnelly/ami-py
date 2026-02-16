"""
Module for detecting AI coding agent environments.
"""

from typing import Literal

from .envvar import using_envvar


def using_claude_code(
    entrypoint: Literal["cli", "claude-desktop", "ide", "remote"] | None = None,
) -> bool:
    """
    Check if running in Claude Code.

    Args:
        entrypoint: Optional entrypoint to check for.
                    If given, checks specifically for that entrypoint.
                    If None, checks for any Claude Code environment.

    Returns:
        bool: True if running in Claude Code (with specified entrypoint if given),
              False otherwise.
    """
    if not using_envvar("CLAUDECODE", "1"):
        return False

    if entrypoint is not None:
        return using_envvar("CLAUDE_CODE_ENTRYPOINT", entrypoint)

    return True


def using_gemini_cli() -> bool:
    """
    Check if running in Gemini CLI.

    Returns:
        bool: True if running in Gemini CLI, False otherwise.
    """
    return using_envvar("GEMINI_CLI", "1")


def using_goose() -> bool:
    """
    Check if running in Goose.

    Returns:
        bool: True if running in Goose, False otherwise.
    """
    return using_envvar("GOOSE_TERMINAL", "1")


def using_opencode() -> bool:
    """
    Check if running in OpenCode.

    Returns:
        bool: True if running in OpenCode, False otherwise.
    """
    return using_envvar("OPENCODE", "1")


def using_coding_agent() -> bool:
    """
    Check if running in any AI coding agent environment.

    Returns:
        bool: True if running in any coding agent environment, False otherwise.
    """
    return (
        using_envvar("AGENT", "1")
        or using_claude_code()
        or using_gemini_cli()
        or using_goose()
        or using_opencode()
    )
