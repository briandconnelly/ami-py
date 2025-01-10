from importlib.metadata import version

__version__ = version("ami")

from .account import using_account
from .ci import (
    using_appveyor,
    using_ci,
    using_circle_ci,
    using_codebuild,
    using_github_actions,
    using_gitlab_ci,
    using_jenkins,
    using_travis_ci,
)
from .conda import using_conda
from .container import (
    using_container,
    using_docker_container,
    using_kubernetes,
    using_podman_container,
)
from .networking import online, using_host
from .virtualenv import using_virtualenv
from .vscode import using_vscode

__all__ = [
    "online",
    "using_account",
    "using_appveyor",
    "using_ci",
    "using_circle_ci",
    "using_codebuild",
    "using_conda",
    "using_container",
    "using_docker_container",
    "using_github_actions",
    "using_gitlab_ci",
    "using_host",
    "using_jenkins",
    "using_kubernetes",
    "using_podman_container",
    "using_travis_ci",
    "using_virtualenv",
    "using_vscode",
]
