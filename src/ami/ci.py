"""
Module for detecting continuous integration environments.
"""

from .envvar import using_envvar


def using_appveyor() -> bool:
    """
    Check if running in AppVeyor CI.

    Returns:
        bool: True if running in AppVeyor, False otherwise.
    """
    return using_envvar("APPVEYOR")


def using_circle_ci() -> bool:
    """
    Check if running in CircleCI.

    Returns:
        bool: True if running in CircleCI, False otherwise.
    """
    return using_envvar("CIRCLECI")


def using_codebuild() -> bool:
    """
    Check if running in AWS CodeBuild.

    Returns:
        bool: True if running in CodeBuild, False otherwise.
    """
    return using_envvar("CODEBUILD_BUILD_ID")


def using_github_actions() -> bool:
    """
    Check if running in GitHub Actions.

    Returns:
        bool: True if running in GitHub Actions, False otherwise.
    """
    return using_envvar("GITHUB_ACTIONS")


def using_gitlab_ci() -> bool:
    """
    Check if running in GitLab CI.

    Returns:
        bool: True if running in GitLab CI, False otherwise.
    """
    return using_envvar("GITLAB_CI")


def using_jenkins() -> bool:
    """
    Check if running in Jenkins.

    Returns:
        bool: True if running in Jenkins, False otherwise.
    """
    return using_envvar("JENKINS_URL")


def using_travis_ci() -> bool:
    """
    Check if running in Travis CI.

    Returns:
        bool: True if running in Travis CI, False otherwise.
    """
    return using_envvar("TRAVIS")


def using_ci() -> bool:
    """
    Check if running in any CI environment.

    Returns:
        bool: True if running in any CI environment, False otherwise.
    """
    return (
        using_envvar("CI")
        or using_appveyor()
        or using_circle_ci()
        or using_codebuild()
        or using_github_actions()
        or using_gitlab_ci()
        or using_jenkins()
        or using_travis_ci()
    )
