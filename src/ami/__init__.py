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
    using_runpod,
)
from .cpu import using_arm_cpu, using_cpu, using_ppc_cpu, using_s390_cpu, using_x86_cpu
from .databricks import using_databricks
from .envvar import using_envvar
from .networking import online, using_host
from .positron import using_positron, using_positron_desktop, using_positron_server
from .python import using_python_version
from .quarto import using_quarto
from .testing import using_pytest, using_tox
from .virtualenv import using_virtualenv
from .vscode import using_vscode

__all__ = [
    "online",
    "using_account",
    "using_appveyor",
    "using_arm_cpu",
    "using_ci",
    "using_circle_ci",
    "using_codebuild",
    "using_conda",
    "using_container",
    "using_cpu",
    "using_databricks",
    "using_docker_container",
    "using_envvar",
    "using_github_actions",
    "using_gitlab_ci",
    "using_host",
    "using_jenkins",
    "using_kubernetes",
    "using_podman_container",
    "using_positron",
    "using_positron_desktop",
    "using_positron_server",
    "using_ppc_cpu",
    "using_pytest",
    "using_python_version",
    "using_quarto",
    "using_runpod",
    "using_s390_cpu",
    "using_travis_ci",
    "using_virtualenv",
    "using_vscode",
    "using_x86_cpu",
    "using_tox",
]
