"""Test function in database."""
import pytest

from dundie.core import add, load, read
from dundie.database import get_session
from dundie.models import Person
from dundie.utils.db import add_person
from tests.constants import PEOPLE_FILE


@pytest.mark.esp
@pytest.mark.unit
def test_add_movement():
    """Test add movement."""
    with get_session() as session:
        data = {
            "name": "Joe Doe",
            "role": "Salesman",
            "dept": "Sales",
            "email": "joe@doe.com",
        }
        joe, created = add_person(session, Person(**data))
        assert created is True

        data = {
            "name": "Jim Doe",
            "role": "Manager",
            "dept": "Management",
            "email": "jim@doe.com",
        }
        jim, created = add_person(session, Person(**data))
        assert created is True

        session.commit()

        add(-30, email="joe@doe.com")
        add(90, dept="Management")
        session.refresh(joe)
        session.refresh(jim)

        assert joe.balance[0].value == 470
        assert jim.balance[0].value == 190


@pytest.mark.unit
def test_add_balance_for_dept():
    """Test add balance for dept."""
    load(PEOPLE_FILE)
    original = read(dept="Sales")

    add(100, dept="Sales")

    modified = read(dept="Sales")
    for index, person in enumerate(modified):
        assert person["balance"] == original[index]["balance"] + 100


@pytest.mark.unit
def test_add_balance_for_person():
    """Test add balance for person."""
    load(PEOPLE_FILE)
    original = read(email="jim@dumdlermifflin.example.com")

    add(-30, email="jim@dumdlermifflin.example.com")

    modified = read(email="jim@dumdlermifflin.example.com")
    for index, person in enumerate(modified):
        assert person["balance"] == original[index]["balance"] - 30
