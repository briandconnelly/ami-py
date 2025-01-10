"""
Tests for the conda module.
"""

from typing import Any

import pytest

from ami.conda import using_conda


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove Conda variables from environment."""
    monkeypatch.delenv("CONDA_DEFAULT_ENV", raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,check_env,expected",
    [
        # Basic detection of any conda environment
        ("CONDA_DEFAULT_ENV", "base", None, True),
        ("CONDA_DEFAULT_ENV", "myenv", None, True),
        ("CONDA_DEFAULT_ENV", "", None, True),
        # Specific environment matching
        ("CONDA_DEFAULT_ENV", "myenv", "myenv", True),
        ("CONDA_DEFAULT_ENV", "myenv", "otherenv", False),
        ("CONDA_DEFAULT_ENV", "base", "base", True),
        # No conda environment
        (None, None, None, False),
        (None, None, "myenv", False),
    ],
)
def test_using_conda(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    check_env: str | None,
    expected: bool,
) -> None:
    """Test Conda environment detection with various configurations."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_conda(check_env) is expected
