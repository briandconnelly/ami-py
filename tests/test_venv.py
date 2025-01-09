import os
import pytest
from ami.virtualenv import using_virtualenv


@pytest.fixture
def clean_env():
    """Fixture to manage VIRTUAL_ENV environment variable state"""
    # Save original environment variable if it exists
    original_env = os.environ.get("VIRTUAL_ENV", None)

    yield  # This is where the test runs

    # Restore original environment variable
    if original_env is not None:
        os.environ["VIRTUAL_ENV"] = original_env
    elif "VIRTUAL_ENV" in os.environ:
        del os.environ["VIRTUAL_ENV"]


def test_no_virtualenv(clean_env):
    """Test when no virtual environment is active"""
    if "VIRTUAL_ENV" in os.environ:
        del os.environ["VIRTUAL_ENV"]
    assert not using_virtualenv()
    assert not using_virtualenv("myenv")


def test_with_virtualenv_no_name(clean_env):
    """Test when a virtual environment is active but no specific name is checked"""
    os.environ["VIRTUAL_ENV"] = "/path/to/myenv"
    assert using_virtualenv()


def test_with_virtualenv_matching_name(clean_env):
    """Test when virtual environment matches the specified name"""
    os.environ["VIRTUAL_ENV"] = "/path/to/myenv"
    assert using_virtualenv("myenv")


def test_with_virtualenv_non_matching_name(clean_env):
    """Test when virtual environment doesn't match the specified name"""
    os.environ["VIRTUAL_ENV"] = "/path/to/myenv"
    assert not using_virtualenv("otherenv")


# Alternative approach using pytest's monkeypatch
def test_with_monkeypatch(monkeypatch):
    """Test using pytest's monkeypatch fixture"""
    monkeypatch.setenv("VIRTUAL_ENV", "/path/to/testenv")
    assert using_virtualenv()
    assert using_virtualenv("testenv")
    assert not using_virtualenv("wrongenv")
