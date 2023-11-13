"""Test core module."""
import pytest

from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_has_n_people():
    """Test load function has correct n peoples."""
    assert len(load(PEOPLE_FILE)) == 3


@pytest.mark.unit
@pytest.mark.high
def test_load_positive_name():
    """Test load function correct name."""
    assert load(PEOPLE_FILE)[0]["name"] == "Jim Halpert"


@pytest.mark.unit
@pytest.mark.high
def test_negative_filenotfound(request):
    """Test file not found."""
    with pytest.raises(FileNotFoundError):
        load("assets/invalid.csv")
