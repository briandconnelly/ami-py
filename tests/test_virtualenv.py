"""
Tests for the virtualenv module.
"""

import os
from pathlib import Path
from typing import Any

import pytest

from ami.virtualenv import using_virtualenv


@pytest.fixture
def clean_env(monkeypatch) -> None:
    """Remove virtualenv variables from environment."""
    test_vars = {"VIRTUAL_ENV"}
    for var in test_vars:
        monkeypatch.delenv(var, raising=False)


def test_using_virtualenv_no_env(clean_env: None, monkeypatch: Any) -> None:
    """Test when no virtualenv is active."""
    assert using_virtualenv() is False
    assert using_virtualenv("/path/to/venv") is False


def test_using_virtualenv_any(clean_env: None, monkeypatch: Any) -> None:
    """Test detection of any virtualenv."""
    monkeypatch.setenv("VIRTUAL_ENV", "/path/to/venv")
    print(f"current value is {os.environ['VIRTUAL_ENV']}")
    assert using_virtualenv() is True


def test_using_virtualenv_specific_path_match(
    clean_env: None, monkeypatch: Any
) -> None:
    """Test matching specific virtualenv path."""
    venv_path = "/path/to/venv"
    monkeypatch.setenv("VIRTUAL_ENV", venv_path)
    assert using_virtualenv(venv_path) is True
    assert using_virtualenv(Path(venv_path)) is True


def test_using_virtualenv_specific_path_no_match(
    clean_env: None, monkeypatch: Any
) -> None:
    """Test non-matching virtualenv path."""
    monkeypatch.setenv("VIRTUAL_ENV", "/path/to/venv1")
    assert using_virtualenv("/path/to/venv2") is False
    assert using_virtualenv(Path("/path/to/venv2")) is False


@pytest.mark.skipif(os.name != "nt", reason="Windows-specific path tests")
def test_using_virtualenv_windows_paths(clean_env: None, monkeypatch: Any) -> None:
    """Test Windows path handling."""
    monkeypatch.setenv("VIRTUAL_ENV", r"C:\Users\test\venv")
    assert using_virtualenv(r"C:\Users\test\venv") is True
    assert using_virtualenv(Path(r"C:\Users\test\venv")) is True
    assert using_virtualenv(r"C:\Users\test\other_venv") is False


@pytest.mark.skipif(os.name == "nt", reason="Unix-specific path tests")
def test_using_virtualenv_unix_paths(clean_env: None, monkeypatch: Any) -> None:
    """Test Unix path handling."""
    monkeypatch.setenv("VIRTUAL_ENV", "/home/user/venv")
    assert using_virtualenv("/home/user/venv") is True
    assert using_virtualenv(Path("/home/user/venv")) is True
    assert using_virtualenv("/home/user/other_venv") is False
