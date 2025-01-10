"""
Tests for the vscode module.
"""

from typing import Any

import pytest

from ami.vscode import using_vscode


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove VS Code variables from environment."""
    monkeypatch.delenv("TERM_PROGRAM", raising=False)


@pytest.mark.parametrize(
    "term_value,expected",
    [
        (None, False),  # TERM_PROGRAM not set
        ("vscode", True),  # VS Code
        ("apple_terminal", False),  # Other terminal
        ("iterm2", False),  # Other terminal
        ("gnome-terminal", False),  # Other terminal
    ],
)
def test_using_vscode(
    clean_env: None, monkeypatch: Any, term_value: str | None, expected: bool
) -> None:
    """Test VS Code detection with various TERM_PROGRAM values."""
    if term_value is not None:
        monkeypatch.setenv("TERM_PROGRAM", term_value)
    assert using_vscode() is expected
