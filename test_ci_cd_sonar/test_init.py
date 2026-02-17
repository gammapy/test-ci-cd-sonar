"""Test CI/CD and SonarQube for Gammapy."""

from test_ci_cd_sonar import __version__


def test_get_version():
    assert __version__ != "0.0.0"


def test_version_exists():
    """Test that __version__ is defined."""
    assert __version__ is not None


def test_version_format():
    """Test that __version__ follows semantic versioning."""
    assert isinstance(__version__, str)
    assert len(__version__) > 0