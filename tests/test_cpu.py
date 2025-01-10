"""
Tests for the cpu module.
"""

import platform
from typing import Any

import pytest

from ami.cpu import (
    using_arm_cpu,
    using_cpu,
    using_ppc_cpu,
    using_s390_cpu,
    using_x86_cpu,
)


@pytest.fixture
def mock_machine(monkeypatch: Any) -> None:
    """Reset platform.machine mocking."""
    monkeypatch.undo()


@pytest.mark.parametrize(
    "machine,expected",
    [
        ("x86_64", True),
        ("amd64", True),
        ("i386", True),
        ("i686", True),
        ("arm64", False),
        ("aarch64", False),
        ("ppc64le", False),
        ("s390x", False),
        ("unknown", False),
    ],
)
def test_using_x86_cpu(
    mock_machine: None, monkeypatch: Any, machine: str, expected: bool
) -> None:
    """Test x86 CPU architecture detection."""
    monkeypatch.setattr(platform, "machine", lambda: machine)
    assert using_x86_cpu() is expected


@pytest.mark.parametrize(
    "machine,expected",
    [
        ("arm64", True),
        ("armv7l", True),
        ("aarch64", True),
        ("x86_64", False),
        ("ppc64le", False),
        ("s390x", False),
        ("unknown", False),
    ],
)
def test_using_arm_cpu(
    mock_machine: None, monkeypatch: Any, machine: str, expected: bool
) -> None:
    """Test ARM CPU architecture detection."""
    monkeypatch.setattr(platform, "machine", lambda: machine)
    assert using_arm_cpu() is expected


@pytest.mark.parametrize(
    "machine,expected",
    [
        ("ppc64le", True),
        ("ppc64", True),
        ("ppc", True),
        ("x86_64", False),
        ("arm64", False),
        ("s390x", False),
        ("unknown", False),
    ],
)
def test_using_ppc_cpu(
    mock_machine: None, monkeypatch: Any, machine: str, expected: bool
) -> None:
    """Test PowerPC CPU architecture detection."""
    monkeypatch.setattr(platform, "machine", lambda: machine)
    assert using_ppc_cpu() is expected


@pytest.mark.parametrize(
    "machine,expected",
    [
        ("s390x", True),
        ("s390", True),
        ("x86_64", False),
        ("arm64", False),
        ("ppc64le", False),
        ("unknown", False),
    ],
)
def test_using_s390_cpu(
    mock_machine: None, monkeypatch: Any, machine: str, expected: bool
) -> None:
    """Test S/390 CPU architecture detection."""
    monkeypatch.setattr(platform, "machine", lambda: machine)
    assert using_s390_cpu() is expected


@pytest.mark.parametrize(
    "machine,arch,expected",
    [
        ("x86_64", "x86", True),
        ("arm64", "arm", True),
        ("ppc64le", "ppc", True),
        ("s390x", "s390", True),
        ("x86_64", "arm", False),
        ("arm64", "x86", False),
        ("unknown", "x86", False),
    ],
)
def test_using_cpu(
    mock_machine: None, monkeypatch: Any, machine: str, arch: str, expected: bool
) -> None:
    """Test generic CPU architecture detection."""
    monkeypatch.setattr(platform, "machine", lambda: machine)
    assert using_cpu(arch) is expected


def test_using_cpu_invalid_arch(mock_machine: None, monkeypatch: Any) -> None:
    """Test invalid architecture handling."""
    monkeypatch.setattr(platform, "machine", lambda: "x86_64")
    with pytest.raises(ValueError, match="Invalid architecture"):
        using_cpu("invalid")  # type: ignore
