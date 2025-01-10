"""
Tests for the testing module.
"""

from typing import Any

import pytest

from ami.testing import using_pytest, using_tox


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove testing-related variables from environment."""
    test_vars = {"PYTEST_CURRENT_TEST", "TOX_ENV_NAME"}
    for var in test_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("PYTEST_CURRENT_TEST", "test_module.py::test_function", True),
        ("PYTEST_CURRENT_TEST", "", True),
        # (None, None, False),
    ],
)
def test_using_pytest(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test pytest detection with various environment configurations."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_pytest() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("TOX_ENV_NAME", "py311", True),
        ("TOX_ENV_NAME", "", True),
        (None, None, False),
    ],
)
def test_using_tox(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test tox detection with various environment configurations."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_tox() is expected
