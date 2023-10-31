"""Test function in database."""
import pytest

from dundie.core import read
from dundie.database import get_session
from dundie.models import Person
from dundie.utils.db import add_person


@pytest.mark.unit
def test_read_with_query():
    """Test read with query."""
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
        "email": "joe@doe.com",
    }
    session = get_session()
    _, created = add_person(session, Person(**data))
    assert created is True

    data = {
        "name": "Jim Doe",
        "role": "CEO",
        "dept": "Manager",
        "email": "jim@doe.com",
    }

    _, created = add_person(session, Person(**data))
    assert created is True
    session.commit()

    response = read()
    assert len(response) == 2

    response = read(dept="Manager")
    assert len(response) == 1
    assert response[0]["name"] == "Jim Doe"

    response = read(email="joe@doe.com")
    assert len(response) == 1
    assert response[0]["name"] == "Joe Doe"
