"""
Tests for the power module.
"""

from typing import Any

import psutil
import pytest

from ami.power import using_ac_power, using_battery_power


@pytest.fixture
def mock_battery(monkeypatch: Any) -> None:
    """Reset battery mocking."""
    monkeypatch.undo()


def test_using_battery_power_on_battery(mock_battery: None, monkeypatch: Any) -> None:
    """Test battery detection when on battery power."""

    class MockBattery:
        power_plugged = False

    def mock_sensors_battery() -> Any:
        return MockBattery()

    monkeypatch.setattr(psutil, "sensors_battery", mock_sensors_battery)
    assert using_battery_power() is True
    assert using_ac_power() is False


def test_using_battery_power_on_ac(mock_battery: None, monkeypatch: Any) -> None:
    """Test battery detection when on AC power."""

    class MockBattery:
        power_plugged = True

    def mock_sensors_battery() -> Any:
        return MockBattery()

    monkeypatch.setattr(psutil, "sensors_battery", mock_sensors_battery)
    assert using_battery_power() is False
    assert using_ac_power() is True


def test_using_battery_power_no_battery(mock_battery: None, monkeypatch: Any) -> None:
    """Test battery detection when no battery is present."""

    def mock_sensors_battery() -> Any:
        return None

    monkeypatch.setattr(psutil, "sensors_battery", mock_sensors_battery)
    assert using_battery_power() is False
    assert using_ac_power() is False


def test_using_battery_power_error(mock_battery: None, monkeypatch: Any) -> None:
    """Test battery detection when an error occurs."""

    def mock_sensors_battery() -> Any:
        raise RuntimeError("Test error")

    monkeypatch.setattr(psutil, "sensors_battery", mock_sensors_battery)
    with pytest.raises(RuntimeError, match="Test error"):
        using_battery_power()
    with pytest.raises(RuntimeError, match="Test error"):
        using_ac_power()
