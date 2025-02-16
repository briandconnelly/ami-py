"""
Tests for the uv module.
"""

from typing import Any

import pytest

from ami.uv import using_uv


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove UV variables from environment."""
    monkeypatch.delenv("UV", raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("UV", "1", True),  # UV enabled
        ("UV", "", True),  # Empty value
        (None, None, False),  # Not in UV
    ],
)
def test_using_uv(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test UV detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_uv() is expected
