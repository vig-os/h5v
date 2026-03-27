"""Example tests for h5v."""


def test_example():
    """Example test that always passes."""
    assert True


def test_import():
    """Test that the package can be imported."""
    import h5v  # noqa: F401 - renamed to project name by init-workspace.sh

    assert h5v.__version__ == "0.1.0"
