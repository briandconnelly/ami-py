"""
Module for detecting power-related information.
"""

import psutil


def using_battery_power() -> bool:
    """
    Check if the system is running on battery power.

    Returns:
        bool: True if running on battery, False if plugged in or no battery present.

    Raises:
        Exception: If there was an error checking the power status.
    """
    battery = psutil.sensors_battery()
    if battery is None:
        return False
    return not battery.power_plugged


def using_ac_power() -> bool:
    """
    Check if the system is running on AC power.

    Returns:
        bool: True if plugged in, False if on battery or no battery present.

    Raises:
        Exception: If there was an error checking the power status.
    """
    battery = psutil.sensors_battery()
    if battery is None:
        return False
    return battery.power_plugged
