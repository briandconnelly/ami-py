"""
Module for detecting operating systems.
"""

import sys
from typing import Literal


def using_aix() -> bool:
    """
    Check if running on AIX.

    Returns:
        bool: True if running on AIX, False otherwise.
    """
    return sys.platform.startswith("aix")


def using_freebsd() -> bool:
    """
    Check if running on FreeBSD.

    Returns:
        bool: True if running on FreeBSD, False otherwise.
    """
    return sys.platform.startswith("freebsd")


def using_linux() -> bool:
    """
    Check if running on Linux.

    Returns:
        bool: True if running on Linux, False otherwise.
    """
    return sys.platform.startswith("linux")


def using_macos() -> bool:
    """
    Check if running on macOS.

    Returns:
        bool: True if running on macOS, False otherwise.
    """
    return sys.platform == "darwin"


def using_netbsd() -> bool:
    """
    Check if running on NetBSD.

    Returns:
        bool: True if running on NetBSD, False otherwise.
    """
    return sys.platform.startswith("netbsd")


def using_openbsd() -> bool:
    """
    Check if running on OpenBSD.

    Returns:
        bool: True if running on OpenBSD, False otherwise.
    """
    return sys.platform.startswith("openbsd")


def using_os(
    name: Literal[
        "AIX",
        "Darwin",
        "FreeBSD",
        "Linux",
        "MacOS",
        "NetBSD",
        "OpenBSD",
        "SunOS",
        "Windows",  # noqa: E501
    ],
) -> bool:  # noqa: E501
    """
    Check if running on a specific operating system.

    Args:
        name: Name of the operating system to check for.
              Must be one of: "AIX", "Darwin", "FreeBSD", "Linux",
              "MacOS", "NetBSD", "OpenBSD", "SunOS", "Windows"

    Returns:
        bool: True if running on the specified OS, False otherwise.

    Raises:
        ValueError: If an invalid OS name is specified.
    """
    os_map = {
        "AIX": using_aix,
        "Darwin": using_macos,
        "FreeBSD": using_freebsd,
        "Linux": using_linux,
        "MacOS": using_macos,
        "NetBSD": using_netbsd,
        "OpenBSD": using_openbsd,
        "SunOS": using_solaris,
        "Windows": using_windows,
    }

    if name not in os_map:
        valid_names = '", "'.join(os_map.keys())
        raise ValueError(f'Invalid OS name: "{name}". Must be one of: "{valid_names}"')

    return os_map[name]()


def using_solaris() -> bool:
    """
    Check if running on Solaris/SunOS.

    Returns:
        bool: True if running on Solaris, False otherwise.
    """
    return sys.platform.startswith(("sunos", "solaris"))


def using_windows() -> bool:
    """
    Check if running on Windows.

    Returns:
        bool: True if running on Windows, False otherwise.
    """
    return sys.platform == "win32"
