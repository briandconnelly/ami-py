"""
Tests for the os module.
"""

import sys
from typing import Any

import pytest

from ami.os import (
    using_aix,
    using_freebsd,
    using_linux,
    using_macos,
    using_netbsd,
    using_openbsd,
    using_os,
    using_solaris,
    using_windows,
)


@pytest.fixture
def mock_platform(monkeypatch: Any) -> None:
    """Reset platform mocking."""
    monkeypatch.undo()


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("aix", True),
        ("aix7", True),
        ("linux", False),
        ("darwin", False),
        ("win32", False),
    ],
)
def test_using_aix(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test AIX detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_aix() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("freebsd12", True),
        ("freebsd13", True),
        ("linux", False),
        ("darwin", False),
        ("win32", False),
    ],
)
def test_using_freebsd(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test FreeBSD detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_freebsd() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("linux", True),
        ("linux2", True),
        ("darwin", False),
        ("win32", False),
        ("aix", False),
    ],
)
def test_using_linux(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test Linux detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_linux() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("darwin", True),
        ("linux", False),
        ("win32", False),
        ("aix", False),
    ],
)
def test_using_macos(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test macOS detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_macos() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("netbsd8", True),
        ("netbsd9", True),
        ("linux", False),
        ("darwin", False),
        ("win32", False),
    ],
)
def test_using_netbsd(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test NetBSD detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_netbsd() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("openbsd6", True),
        ("openbsd7", True),
        ("linux", False),
        ("darwin", False),
        ("win32", False),
    ],
)
def test_using_openbsd(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test OpenBSD detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_openbsd() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("sunos5", True),
        ("solaris2.7", True),
        ("linux", False),
        ("darwin", False),
        ("win32", False),
    ],
)
def test_using_solaris(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test Solaris detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_solaris() is expected


@pytest.mark.parametrize(
    "platform_name,expected",
    [
        ("win32", True),
        ("linux", False),
        ("darwin", False),
        ("aix", False),
    ],
)
def test_using_windows(
    mock_platform: None, monkeypatch: Any, platform_name: str, expected: bool
) -> None:
    """Test Windows detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_windows() is expected


@pytest.mark.parametrize(
    "platform_name,check_name,expected",
    [
        ("linux", "Linux", True),
        ("darwin", "Darwin", True),
        ("darwin", "MacOS", True),
        ("win32", "Windows", True),
        ("aix", "AIX", True),
        ("freebsd12", "FreeBSD", True),
        ("netbsd8", "NetBSD", True),
        ("openbsd6", "OpenBSD", True),
        ("sunos5", "SunOS", True),
        # Non-matching tests
        ("linux", "Windows", False),
        ("darwin", "Linux", False),
        ("win32", "Darwin", False),
    ],
)
def test_using_os(
    mock_platform: None,
    monkeypatch: Any,
    platform_name: str,
    check_name: str,
    expected: bool,
) -> None:
    """Test generic OS detection."""
    monkeypatch.setattr(sys, "platform", platform_name)
    assert using_os(check_name) is expected


def test_using_os_invalid_name(mock_platform: None, monkeypatch: Any) -> None:
    """Test invalid OS name handling."""
    monkeypatch.setattr(sys, "platform", "linux")
    with pytest.raises(ValueError, match="Invalid OS name"):
        using_os("InvalidOS")  # type: ignore
