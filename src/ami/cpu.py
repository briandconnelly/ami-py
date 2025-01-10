"""
Module for detecting CPU architectures.
"""

import platform
from typing import Literal


def using_x86_cpu() -> bool:
    """
    Check if running on x86/x86_64 CPU architecture.

    Returns:
        bool: True if running on x86/x86_64, False otherwise.
    """
    machine = platform.machine().lower()
    return machine in ("x86_64", "amd64", "i386", "i686")


def using_arm_cpu() -> bool:
    """
    Check if running on ARM CPU architecture.

    Returns:
        bool: True if running on ARM, False otherwise.
    """
    machine = platform.machine().lower()
    return machine.startswith("arm") or machine.startswith("aarch")


def using_ppc_cpu() -> bool:
    """
    Check if running on PowerPC CPU architecture.

    Returns:
        bool: True if running on PowerPC, False otherwise.
    """
    machine = platform.machine().lower()
    return machine.startswith("ppc")


def using_s390_cpu() -> bool:
    """
    Check if running on IBM S/390 CPU architecture.

    Returns:
        bool: True if running on S/390, False otherwise.
    """
    machine = platform.machine().lower()
    return machine.startswith("s390")


def using_cpu(arch: Literal["x86", "arm", "ppc", "s390"]) -> bool:
    """
    Check if running on a specific CPU architecture.

    Args:
        arch: The CPU architecture to check for.
              Must be one of: "x86", "arm", "ppc", "s390"

    Returns:
        bool: True if running on the specified architecture, False otherwise.

    Raises:
        ValueError: If an invalid architecture is specified.
    """
    arch_map = {
        "x86": using_x86_cpu,
        "arm": using_arm_cpu,
        "ppc": using_ppc_cpu,
        "s390": using_s390_cpu,
    }

    if arch not in arch_map:
        valid_archs = '", "'.join(arch_map.keys())
        raise ValueError(
            f'Invalid architecture: "{arch}". Must be one of: "{valid_archs}"'
        )

    return arch_map[arch]()
