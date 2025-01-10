"""
Tests for the container module.
"""

import os
from typing import Any

import pytest

from ami.container import (
    using_container,
    using_docker_container,
    using_kubernetes,
    using_podman_container,
)


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove container-related variables from environment."""
    monkeypatch.delenv("KUBERNETES_SERVICE_HOST", raising=False)


@pytest.mark.parametrize(
    "dockerenv_exists,containerenv_exists,expected",
    [
        (True, False, True),  # Docker container
        (False, True, True),  # Podman container
        (True, True, True),  # Both exist
        (False, False, False),  # Neither exist
    ],
)
def test_using_container(
    clean_env: None,
    monkeypatch: Any,
    tmp_path: Any,
    dockerenv_exists: bool,
    containerenv_exists: bool,
    expected: bool,
) -> None:
    """Test container detection."""

    # Mock path.exists for container files
    def mock_exists(path: str) -> bool:
        if path == "/.dockerenv":
            return dockerenv_exists
        if path == "/run/.containerenv":
            return containerenv_exists
        return os.path.exists(path)

    monkeypatch.setattr(os.path, "exists", mock_exists)
    assert using_container() is expected


@pytest.mark.parametrize(
    "dockerenv_exists,expected",
    [
        (True, True),  # Docker container
        (False, False),  # Not a Docker container
    ],
)
def test_using_docker_container(
    clean_env: None, monkeypatch: Any, dockerenv_exists: bool, expected: bool
) -> None:
    """Test Docker container detection."""

    # Mock path.exists for .dockerenv
    def mock_exists(path: str) -> bool:
        if path == "/.dockerenv":
            return dockerenv_exists
        return os.path.exists(path)

    monkeypatch.setattr(os.path, "exists", mock_exists)
    assert using_docker_container() is expected


@pytest.mark.parametrize(
    "containerenv_exists,expected",
    [
        (True, True),  # Podman container
        (False, False),  # Not a Podman container
    ],
)
def test_using_podman_container(
    clean_env: None, monkeypatch: Any, containerenv_exists: bool, expected: bool
) -> None:
    """Test Podman container detection."""

    # Mock path.exists for .containerenv
    def mock_exists(path: str) -> bool:
        if path == "/run/.containerenv":
            return containerenv_exists
        return os.path.exists(path)

    monkeypatch.setattr(os.path, "exists", mock_exists)
    assert using_podman_container() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("KUBERNETES_SERVICE_HOST", "10.0.0.1", True),  # K8s environment
        ("KUBERNETES_SERVICE_HOST", "", True),  # Empty value
        (None, None, False),  # No K8s environment
    ],
)
def test_using_kubernetes(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Kubernetes detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_kubernetes() is expected
