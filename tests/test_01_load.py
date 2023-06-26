import pytest
from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.mark.unit
def test_load():
    """Test load function"""
    assert len(load(PEOPLE_FILE))== 2
    assert load(PEOPLE_FILE)[0][0]=='J'