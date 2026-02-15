import socket


def online(host: str = "8.8.8.8", port: int = 53, timeout: float = 3.0) -> bool:
    """
    Check if the machine is connected to the internet.

    Args:
        host: Host to connect to for the check. Defaults to Google's DNS server.
        port: Port to connect to. Defaults to 53 (DNS).
        timeout: Connection timeout in seconds. Defaults to 3.0.

    Returns:
        bool: True if there is an internet connection, False otherwise
    """
    try:
        socket.create_connection((host, port), timeout=timeout)
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
