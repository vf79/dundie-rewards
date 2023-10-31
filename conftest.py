"""Config file to pytest."""

import pytest
from unittest.mock import patch
from sqlmodel import create_engine
from dundie import models

MARKER = """\
unit: Mark unit tests
integration: Mark integration tests
high: High Priority
medium: Medium Priority
low: Low Priority
run: Priority now
"""


def pytest_configure(config):
    """Get markers config."""
    for line in MARKER.split("\n"):
        config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):
    """Set tmp directory."""
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # protocolo de generators


@pytest.fixture(autouse=True, scope="function")
def setup_testing_database(request):
    """Set test database.

    For each test, create a database file on tmpdir.
    Force database.py to that file.
    """
    tmpdir = request.getfixturevalue("tmpdir")
    test_db = str(tmpdir.join("database.test.db"))
    engine = create_engine(f"sqlite:///{test_db}")
    models.SQLModel.metadata.create_all(bind=engine)
    with patch("dundie.database.engine", engine):
        yield
