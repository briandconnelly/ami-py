"""
Tests for the python module.
"""

import sys
from typing import Any, Union

import pytest

from ami.python import using_python_version


def get_current_version() -> tuple[int, ...]:
    """Get current Python version as a tuple."""
    return sys.version_info[:3]


@pytest.mark.parametrize(
    "version,expected",
    [
        # Basic version checks
        (f"{sys.version_info[0]}.{sys.version_info[1]}", True),  # Current version
        (
            f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}",
            True,
        ),  # Full version
        ((sys.version_info[0], sys.version_info[1]), True),  # Current tuple
        (
            (sys.version_info[0], sys.version_info[1], sys.version_info[2]),
            True,
        ),  # Full tuple
        # Comparison operators
        (f">={sys.version_info[0]}.{sys.version_info[1]}", True),  # Current or newer
        (f"<={sys.version_info[0]}.{sys.version_info[1]}", True),  # Current or older
        (f">{sys.version_info[0]}.{sys.version_info[1] - 1}", True),  # Previous minor
        (f"<{sys.version_info[0]}.{sys.version_info[1] + 1}", True),  # Next minor
        (f"!={sys.version_info[0]}.{sys.version_info[1] - 1}", True),  # Not previous
        # Non-matching versions
        (f"{sys.version_info[0]}.{sys.version_info[1] + 1}", False),  # Future version
        (f"{sys.version_info[0]}.{sys.version_info[1] - 1}", False),  # Past version
        ((sys.version_info[0], sys.version_info[1] + 1), False),  # Future tuple
        ((sys.version_info[0], sys.version_info[1] - 1), False),  # Past tuple
    ],
)
def test_using_python_version(
    version: Union[str, tuple[int, ...]], expected: bool
) -> None:
    """Test Python version detection with various version formats."""
    assert using_python_version(version) is expected


@pytest.mark.parametrize(
    "version",
    [
        "3",  # Missing minor version
        "3.11.0.0",  # Too many version parts
        (3,),  # Tuple too short
        (3, 11, 0, 0),  # Tuple too long
        "3.11.a",  # Invalid version number
        ">=3.11.0.0",  # Too many version parts with operator
        ">>3.11",  # Invalid operator
        "3.11>=",  # Operator in wrong position
        None,  # None
        123,  # Integer
        3.11,  # Float
        ["3", "11"],  # List
        {"version": "3.11"},  # Dict
    ],
)
def test_using_python_version_invalid(version: Any) -> None:
    """Test Python version detection with invalid version formats."""
    with pytest.raises(ValueError):
        using_python_version(version)
