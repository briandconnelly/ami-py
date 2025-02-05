"""
Tests for the github module.
"""

from typing import Any

import pytest

from ami.github import using_github_actions, using_github_codespaces


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove GitHub variables from environment."""
    github_vars = {"GITHUB_ACTIONS", "CODESPACES", "CODESPACE_NAME"}
    for var in github_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("GITHUB_ACTIONS", "true", True),  # Actions enabled
        ("GITHUB_ACTIONS", "", True),  # Empty value
        (None, None, False),  # Not in Actions
    ],
)
def test_using_github_actions(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test GitHub Actions detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_github_actions() is expected


@pytest.mark.parametrize(
    "codespaces,name_value,check_name,expected",
    [
        ("true", "my-space", None, True),  # In Codespaces, no name check
        ("true", "my-space", "my-space", True),  # Matching name
        ("true", "my-space", "other-space", False),  # Non-matching name
        ("true", "", None, True),  # Empty name, no check
        ("true", "", "", True),  # Empty name match
        ("", "my-space", None, False),  # Codespaces not set
        (None, None, None, False),  # Not in Codespaces
        (None, None, "my-space", False),  # Not in Codespaces with name
    ],
)
def test_using_github_codespaces(
    clean_env: None,
    monkeypatch: Any,
    codespaces: str | None,
    name_value: str | None,
    check_name: str | None,
    expected: bool,
) -> None:
    """Test GitHub Codespaces detection."""
    if codespaces is not None:
        monkeypatch.setenv("CODESPACES", codespaces)
    if name_value is not None:
        monkeypatch.setenv("CODESPACE_NAME", name_value)
    assert using_github_codespaces(check_name) is expected
