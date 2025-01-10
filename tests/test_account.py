"""
Tests for the account module.
"""

import getpass
from typing import Any

import pytest

from ami.account import using_account


@pytest.fixture
def mock_getuser(monkeypatch: Any) -> None:
    """Remove any mocked username."""
    monkeypatch.undo()


def test_using_account_match(mock_getuser: None, monkeypatch: Any) -> None:
    """Test when username matches."""
    monkeypatch.setattr(getpass, "getuser", lambda: "testuser")
    assert using_account("testuser") is True


def test_using_account_no_match(mock_getuser: None, monkeypatch: Any) -> None:
    """Test when username doesn't match."""
    monkeypatch.setattr(getpass, "getuser", lambda: "testuser")
    assert using_account("otheruser") is False


def test_using_account_case_sensitive(mock_getuser: None, monkeypatch: Any) -> None:
    """Test that username matching is case-sensitive."""
    monkeypatch.setattr(getpass, "getuser", lambda: "TestUser")
    assert using_account("testuser") is False
    assert using_account("TestUser") is True
    assert using_account("TESTUSER") is False


def test_using_account_special_chars(mock_getuser: None, monkeypatch: Any) -> None:
    """Test usernames with special characters."""
    monkeypatch.setattr(getpass, "getuser", lambda: "test.user")
    assert using_account("test.user") is True
    assert using_account("test_user") is False


@pytest.mark.parametrize(
    "username",
    [
        "normal_user",  # Unix-style
        "user.name",  # With dot
        "user-name",  # With hyphen
        "UserName",  # Windows-style
        "SYSTEM",  # Windows system account
        "user@domain",  # Domain user
    ],
)
def test_using_account_platform_usernames(
    mock_getuser: None, monkeypatch: Any, username: str
) -> None:
    """Test various platform-specific username formats."""
    monkeypatch.setattr(getpass, "getuser", lambda: username)
    assert using_account(username) is True
