"""
Tests for the coding_agent module.
"""

from typing import Any

import pytest

from ami.coding_agent import (
    using_claude_code,
    using_coding_agent,
    using_gemini_cli,
    using_goose,
    using_opencode,
)


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove coding agent variables from environment."""
    for var in (
        "AGENT",
        "CLAUDECODE",
        "CLAUDE_CODE_ENTRYPOINT",
        "GEMINI_CLI",
        "GOOSE_TERMINAL",
        "OPENCODE",
    ):
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "claudecode,entrypoint_env,entrypoint_arg,expected",
    [
        ("1", None, None, True),  # CLAUDECODE=1, no entrypoint check
        ("1", "cli", None, True),  # CLAUDECODE=1 with entrypoint set, no check
        ("1", "cli", "cli", True),  # Matching entrypoint
        ("1", "ide", "cli", False),  # Non-matching entrypoint
        ("1", None, "cli", False),  # Entrypoint check but env not set
        ("0", None, None, False),  # CLAUDECODE != 1
        (None, None, None, False),  # CLAUDECODE not set
        (None, "cli", None, False),  # Entrypoint set but CLAUDECODE not set
        ("1", "claude-desktop", "claude-desktop", True),  # Desktop entrypoint
        ("1", "remote", "remote", True),  # Remote entrypoint
    ],
)
def test_using_claude_code(
    clean_env: None,
    monkeypatch: Any,
    claudecode: str | None,
    entrypoint_env: str | None,
    entrypoint_arg: str | None,
    expected: bool,
) -> None:
    """Test Claude Code detection."""
    if claudecode is not None:
        monkeypatch.setenv("CLAUDECODE", claudecode)
    if entrypoint_env is not None:
        monkeypatch.setenv("CLAUDE_CODE_ENTRYPOINT", entrypoint_env)
    assert using_claude_code(entrypoint_arg) is expected


@pytest.mark.parametrize(
    "env_value,expected",
    [
        ("1", True),
        ("0", False),
        ("", False),
        (None, False),
    ],
)
def test_using_gemini_cli(
    clean_env: None,
    monkeypatch: Any,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Gemini CLI detection."""
    if env_value is not None:
        monkeypatch.setenv("GEMINI_CLI", env_value)
    assert using_gemini_cli() is expected


@pytest.mark.parametrize(
    "env_value,expected",
    [
        ("1", True),
        ("0", False),
        ("", False),
        (None, False),
    ],
)
def test_using_goose(
    clean_env: None,
    monkeypatch: Any,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Goose detection."""
    if env_value is not None:
        monkeypatch.setenv("GOOSE_TERMINAL", env_value)
    assert using_goose() is expected


@pytest.mark.parametrize(
    "env_value,expected",
    [
        ("1", True),
        ("0", False),
        ("", False),
        (None, False),
    ],
)
def test_using_opencode(
    clean_env: None,
    monkeypatch: Any,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test OpenCode detection."""
    if env_value is not None:
        monkeypatch.setenv("OPENCODE", env_value)
    assert using_opencode() is expected


@pytest.mark.parametrize(
    "agent_vars,expected",
    [
        ({"AGENT": "1"}, True),  # Generic AGENT
        ({"CLAUDECODE": "1"}, True),  # Claude Code
        ({"GEMINI_CLI": "1"}, True),  # Gemini CLI
        ({"GOOSE_TERMINAL": "1"}, True),  # Goose
        ({"OPENCODE": "1"}, True),  # OpenCode
        ({"AGENT": "0"}, False),  # AGENT != 1
        ({}, False),  # No agent
    ],
)
def test_using_coding_agent(
    clean_env: None,
    monkeypatch: Any,
    agent_vars: dict[str, str],
    expected: bool,
) -> None:
    """Test generic coding agent detection."""
    for var, value in agent_vars.items():
        monkeypatch.setenv(var, value)
    assert using_coding_agent() is expected
