"""
Module for user account detection and functionality.
"""

import getpass


def using_account(username: str) -> bool:
    """
    Check if running under a specific user account.

    Args:
        username: The username to check against.

    Returns:
        bool: True if running under the specified username, False otherwise.
    """
    return getpass.getuser() == username
