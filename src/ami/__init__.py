from importlib.metadata import version

__version__ = version("ami")

from .networking import online, using_host
from .virtualenv import using_virtualenv
from .vscode import using_vscode

__all__ = [
    "online",
    "using_host",
    "using_virtualenv",
    "using_vscode",
]
