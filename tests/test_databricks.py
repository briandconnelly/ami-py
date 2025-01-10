"""
Tests for the databricks module.
"""

from typing import Any

import pytest

from ami.databricks import using_databricks


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove Databricks variables from environment."""
    monkeypatch.delenv("DATABRICKS_RUNTIME_VERSION", raising=False)


@pytest.mark.parametrize(
    "version,expected",
    [
        ("13.3.x-cpu-ml-scala2.12", True),  # ML runtime
        ("13.3.x-scala2.12", True),  # Standard runtime
        ("11.3.x-photon-scala2.12", True),  # Photon runtime
        ("10.4.x-gpu-ml-scala2.12", True),  # GPU runtime
        ("", True),  # Empty version
        (None, False),  # No runtime version set
    ],
)
def test_using_databricks(
    clean_env: None, monkeypatch: Any, version: str | None, expected: bool
) -> None:
    """Test Databricks detection with various runtime versions."""
    if version is not None:
        monkeypatch.setenv("DATABRICKS_RUNTIME_VERSION", version)
    assert using_databricks() is expected
