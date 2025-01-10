"""
Tests for the ci module.
"""

from typing import Any

import pytest

from ami.ci import (
    using_appveyor,
    using_ci,
    using_circle_ci,
    using_codebuild,
    using_github_actions,
    using_gitlab_ci,
    using_jenkins,
    using_travis_ci,
)


@pytest.fixture
def clean_env(monkeypatch: Any) -> None:
    """Remove CI variables from environment."""
    ci_vars = {
        "CI",
        "APPVEYOR",
        "CIRCLECI",
        "CODEBUILD_BUILD_ID",
        "GITHUB_ACTIONS",
        "GITLAB_CI",
        "JENKINS_URL",
        "TRAVIS",
    }
    for var in ci_vars:
        monkeypatch.delenv(var, raising=False)


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("APPVEYOR", "True", True),
        ("APPVEYOR", "", True),
        (None, None, False),
    ],
)
def test_using_appveyor(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test AppVeyor detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_appveyor() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("CIRCLECI", "True", True),
        ("CIRCLECI", "", True),
        (None, None, False),
    ],
)
def test_using_circle_ci(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test CircleCI detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_circle_ci() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("CODEBUILD_BUILD_ID", "build-id", True),
        ("CODEBUILD_BUILD_ID", "", True),
        (None, None, False),
    ],
)
def test_using_codebuild(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test AWS CodeBuild detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_codebuild() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("GITHUB_ACTIONS", "True", True),
        ("GITHUB_ACTIONS", "", True),
        (None, None, False),
    ],
)
def test_using_github_actions(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test GitHub Actions detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_github_actions() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("GITLAB_CI", "True", True),
        ("GITLAB_CI", "", True),
        (None, None, False),
    ],
)
def test_using_gitlab_ci(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test GitLab CI detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_gitlab_ci() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("JENKINS_URL", "http://jenkins.example.com", True),
        ("JENKINS_URL", "", True),
        (None, None, False),
    ],
)
def test_using_jenkins(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Jenkins detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_jenkins() is expected


@pytest.mark.parametrize(
    "env_var,env_value,expected",
    [
        ("TRAVIS", "True", True),
        ("TRAVIS", "", True),
        (None, None, False),
    ],
)
def test_using_travis_ci(
    clean_env: None,
    monkeypatch: Any,
    env_var: str | None,
    env_value: str | None,
    expected: bool,
) -> None:
    """Test Travis CI detection."""
    if env_var is not None and env_value is not None:
        monkeypatch.setenv(env_var, env_value)
    assert using_travis_ci() is expected


@pytest.mark.parametrize(
    "ci_vars,expected",
    [
        ({"CI": "true"}, True),  # Generic CI
        ({"GITHUB_ACTIONS": "true"}, True),  # GitHub Actions
        ({"GITLAB_CI": "true"}, True),  # GitLab CI
        ({"TRAVIS": "true"}, True),  # Travis CI
        ({}, False),  # No CI
    ],
)
def test_using_ci(
    clean_env: None, monkeypatch: Any, ci_vars: dict[str, str], expected: bool
) -> None:
    """Test generic CI detection."""
    for var, value in ci_vars.items():
        monkeypatch.setenv(var, value)
    assert using_ci() is expected
