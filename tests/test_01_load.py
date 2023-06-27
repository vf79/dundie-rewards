import pytest
import uuid
import os
from dundie.core import load
from tests.constants import PEOPLE_FILE


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    tmp_file = tmpdir.join("new_file.txt")
    tmp_file.write("isso é sujeira...")
    yield
    tmp_file.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test load function"""
    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(lambda: os.unlink(filepath))

    with open(filepath, "w")as indsjd_file:
        indsjd_file.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE))== 2
    assert load(PEOPLE_FILE)[0][0]=='J'


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test load function"""
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w")as indsjd_file:
        indsjd_file.write("dados uteis somente para o teste")

    assert len(load(PEOPLE_FILE))== 2
    assert load(PEOPLE_FILE)[0][0]=='J'