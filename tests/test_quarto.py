"""
Tests for the quarto module.
"""

from typing import Any

import pytest

from ami.quarto import using_quarto


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove Quarto variables from environment."""
    quarto_vars = {
        "QUARTO_DOCUMENT_PATH",
        "QUARTO_PROJECT_ROOT",
        "QUARTO_PROFILE",
        "QUARTO_FIG_WIDTH",
        "QUARTO_FIG_HEIGHT",
        "QUARTO_RUN_NO_NETWORK",
    }
    for var in quarto_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("QUARTO_DOCUMENT_PATH", "/path/to/doc.qmd", True),
        ("QUARTO_PROJECT_ROOT", "/path/to/project", True),
        ("QUARTO_PROFILE", "default", True),
        ("QUARTO_FIG_WIDTH", "6", True),
        ("QUARTO_FIG_HEIGHT", "4", True),
        ("QUARTO_RUN_NO_NETWORK", "true", True),
        ("QUARTO_DOCUMENT_PATH", "", True),
        # Test when no variables are set
        (None, None, False),
    ],
)
def test_using_quarto(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Quarto detection with various environment configurations."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_quarto() is expected
