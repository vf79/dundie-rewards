import pytest

from dundie.core import add
from dundie.database import add_person, commit, connect


@pytest.mark.run
@pytest.mark.unit
def test_add_movement():
    pk = "joe@doe.com"
    data = {
        "name": "Joe Doe",
        "role": "Salesman",
        "dept": "Sales",
        "active": True,
    }
    db = connect()
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    pk = "jim@doe.com"
    data = {
        "name": "Jim Doe",
        "role": "CEO",
        "dept": "Manager",
        "active": True,
    }
    _, created = add_person(db, pk, data)
    assert created is True
    commit(db)

    db = connect()

    add(-30, email="joe@doe.com")
    add(90, dept="Manager")

    db = connect()
    assert db["balance"]["joe@doe.com"] == 470
    assert db["balance"]["jim@doe.com"] == 590
