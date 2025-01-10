import socket


def online() -> bool:
    """
    Check if the machine is connected to the internet.

    Returns:
        bool: True if there is an internet connection, False otherwise
    """
    try:
        # Attempt to connect to a reliable host (Google's DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except (OSError, TimeoutError):
        return False


def using_host(hostname: str) -> bool:
    """
    Check if the machine's hostname matches the specified hostname.

    Args:
        hostname (str): Hostname to check against.

    Returns:
        bool: True if the machine's hostname matches the specified hostname,
              False otherwise
    """
    return socket.gethostname() == hostname
