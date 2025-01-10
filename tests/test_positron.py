"""
Tests for the positron module.
"""

from typing import Any

import pytest

from ami.positron import using_positron, using_positron_desktop, using_positron_server


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove Positron variables from environment."""
    monkeypatch.delenv("POSITRON_MODE", raising=False)


@pytest.mark.parametrize(
    "mode_value,check_mode,expected",
    [
        ("desktop", None, True),  # Desktop mode, no specific check
        ("server", None, True),  # Server mode, no specific check
        ("desktop", "desktop", True),  # Desktop mode, checking desktop
        ("server", "server", True),  # Server mode, checking server
        ("desktop", "server", False),  # Desktop mode, checking server
        ("server", "desktop", False),  # Server mode, checking desktop
        ("", None, True),  # Empty value, no specific check
        (None, None, False),  # No mode set
    ],
)
def test_using_positron(
    clean_env: None,
    monkeypatch: Any,
    mode_value: str | None,
    check_mode: str | None,
    expected: bool,
) -> None:
    """Test Positron IDE detection with various modes."""
    if mode_value is not None:
        monkeypatch.setenv("POSITRON_MODE", mode_value)
    assert using_positron(check_mode) is expected


@pytest.mark.parametrize(
    "mode_value,expected",
    [
        ("desktop", True),  # Desktop mode
        ("server", False),  # Server mode
        ("", False),  # Empty value
        (None, False),  # No mode set
    ],
)
def test_using_positron_desktop(
    clean_env: None, monkeypatch: Any, mode_value: str | None, expected: bool
) -> None:
    """Test Positron Desktop IDE detection."""
    if mode_value is not None:
        monkeypatch.setenv("POSITRON_MODE", mode_value)
    assert using_positron_desktop() is expected


@pytest.mark.parametrize(
    "mode_value,expected",
    [
        ("server", True),  # Server mode
        ("desktop", False),  # Desktop mode
        ("", False),  # Empty value
        (None, False),  # No mode set
    ],
)
def test_using_positron_server(
    clean_env: None, monkeypatch: Any, mode_value: str | None, expected: bool
) -> None:
    """Test Positron Server IDE detection."""
    if mode_value is not None:
        monkeypatch.setenv("POSITRON_MODE", mode_value)
    assert using_positron_server() is expected
