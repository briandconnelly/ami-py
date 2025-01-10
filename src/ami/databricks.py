"""
Module for detecting Databricks environments.
"""

from .envvar import using_envvar


def using_databricks() -> bool:
    """
    Check if running in a Databricks environment.

    Returns:
        bool: True if running in Databricks, False otherwise.
    """
    return using_envvar("DATABRICKS_RUNTIME_VERSION")
