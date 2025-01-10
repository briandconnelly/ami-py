"""
Tests for the networking module.
"""

import socket
from typing import Any

import pytest

from ami.networking import using_host


@pytest.fixture
def mock_socket(monkeypatch: Any) -> None:
    """Reset socket mocking."""
    monkeypatch.undo()


@pytest.mark.parametrize(
    "hostname,current_host,expected",
    [
        ("localhost", "localhost", True),  # Exact match
        ("host1", "host2", False),  # Different hostname
        ("", "localhost", False),  # Empty hostname
    ],
)
def test_using_host(
    mock_socket: None,
    monkeypatch: Any,
    hostname: str,
    current_host: str,
    expected: bool,
) -> None:
    """Test hostname detection."""
    monkeypatch.setattr(socket, "gethostname", lambda: current_host)
    assert using_host(hostname) is expected
