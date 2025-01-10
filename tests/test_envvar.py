"""
Tests for the envvar module.
"""

import sys
from typing import Any

import pytest

from ami.envvar import using_envvar


@pytest.fixture
def clean_env(monkeypatch) -> None:
    """Remove test variables from environment."""
    test_vars = {"TEST_VAR", "EMPTY_VAR", "NUMBER_VAR", "MIXED_CASE_VAR"}
    print("Cleaning the environment...")
    for var in test_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "var_name,var_value,expected",
    [
        ("TEST_VAR", "value", True),  # Basic existence check
        ("NONEXISTENT_VAR", None, False),  # Non-existent variable
        ("EMPTY_VAR", "", True),  # Empty string value
        ("NUMBER_VAR", "123", True),  # Numeric string value
    ],
)
def test_using_envvar_existence(
    clean_env: None,
    monkeypatch: Any,
    var_name: str,
    var_value: str | None,
    expected: bool,
) -> None:
    """Test basic environment variable existence checking."""
    if var_value is not None:
        monkeypatch.setenv(var_name, var_value)
    assert using_envvar(var_name) == expected


@pytest.mark.parametrize(
    "var_name,var_value,check_value,expected",
    [
        ("TEST_VAR", "value", "value", True),  # Exact match
        ("TEST_VAR", "value", "other", False),  # Non-matching value
        ("TEST_VAR", 123, "123", True),  # Env vars are always strings
        ("TEST_VAR", 123, 123, False),
        ("TEST_VAR", True, "True", True),
        ("TEST_VAR", True, True, False),
        ("EMPTY_VAR", "", "", True),  # Empty string match
    ],
)
def test_using_envvar_value_matching(
    clean_env: None,
    monkeypatch: Any,
    var_name: str,
    var_value: str,
    check_value: Any,
    expected: bool,
) -> None:
    """Test using_envvar() produces expected results."""
    monkeypatch.setenv(var_name, str(var_value))
    assert using_envvar(var_name, check_value) == expected


def test_using_envvar_none_value(clean_env: None, monkeypatch: Any) -> None:
    """Test that None check_value only checks existence."""
    monkeypatch.setenv("TEST_VAR", "any_value")
    assert using_envvar("TEST_VAR", None) is True


@pytest.mark.skipif(sys.platform == "win32", reason="This test does not run on Windows")
def test_using_envvar_case_sensitivity(clean_env: None, monkeypatch: Any) -> None:
    """Test case-sensitive value matching on non-Windows machines"""
    monkeypatch.setenv("MIXED_CASE_VAR", "MiXeD_CaSe")
    assert using_envvar("MIXED_CASE_VAR", "mixed_case") is False
    assert using_envvar("MIXED_CASE_VAR", "MIXED_CASE") is False
    assert using_envvar("MIXED_CASE_VAR", "MiXeD_CaSe") is True


@pytest.mark.skipif(sys.platform != "win32", reason="This test only runs on Windows")
def test_using_envvar_case_sensitivity_win(clean_env: None, monkeypatch: Any) -> None:
    """Test case-insensitive value matching on Windows machines"""
    monkeypatch.setenv("MIXED_CASE_VAR", "MiXeD_CaSe")
    assert using_envvar("MIXED_CASE_VAR", "mixed_case") is True
    assert using_envvar("MIXED_CASE_VAR", "MIXED_CASE") is True
    assert using_envvar("MIXED_CASE_VAR", "MiXeD_CaSe") is True
