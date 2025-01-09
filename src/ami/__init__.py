from importlib.metadata import version

__version__ = version("ami")

from .virtualenv import using_virtualenv
from .vscode import using_vscode

__all__ = [
    "using_virtualenv",
    "using_vscode",
]
