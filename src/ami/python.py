"""
Module for detecting Python environment details.
"""

import operator
import sys
from typing import Union


def using_python_version(ver: Union[str, tuple[int, ...]]) -> bool:
    """
    Check if running on a specific Python version.

    Args:
        ver: Python version to check against. Can be:
             - String with optional comparison operator:
               "3.11", ">=3.11", "<=3.11.0", etc.
             - Tuple: (3, 11), (3, 11, 0), etc.

    Returns:
        bool: True if running on the specified version, False otherwise.

    Raises:
        ValueError: If version format is invalid.
    """
    current = sys.version_info[:3]  # Major, minor, micro
    ops = {
        ">=": operator.ge,
        "<=": operator.le,
        ">": operator.gt,
        "<": operator.lt,
        "==": operator.eq,
        "!=": operator.ne,
    }

    # Handle string input (e.g., "3.11", ">=3.11", or "3.11.0")
    if isinstance(ver, str):
        # Check for comparison operator
        for op_str, op_func in ops.items():
            if ver.startswith(op_str):
                version_str = ver[len(op_str) :].strip()
                parts = tuple(int(v) for v in version_str.split("."))
                if len(parts) not in (2, 3):
                    raise ValueError(
                        'Invalid version string. Must be in format "X.Y" or "X.Y.Z"'
                    )
                return op_func(current[: len(parts)], parts)

        # No operator found, use equality comparison
        parts = tuple(int(v) for v in ver.split("."))
        if len(parts) not in (2, 3):
            raise ValueError(
                'Invalid version string. Must be in format "X.Y" or "X.Y.Z"'
            )
        return current[: len(parts)] == parts

    # Handle tuple input (e.g., (3, 11) or (3, 11, 0))
    if isinstance(ver, tuple):
        if not 2 <= len(ver) <= 3:
            raise ValueError(
                "Invalid version tuple. Must contain 2 or 3 integers (major, minor[, micro])" # noqa: E501
            )
        return current[: len(ver)] == ver

    raise ValueError('Version must be a string ("3.11") or tuple((3, 11))')