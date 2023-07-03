"""Core module of dundie"""
from csv import reader

from dundie.database import add_person, commit, connect
from dundie.utils.log import get_logger

log = get_logger()


def load(filepath):
    """Loads data from filepath to the database
    Exemplo de doctest
    Para executar: python -m doctest -v dundie/core.py
    >>> len(load('assets/people.csv'))
    2
    >>> load('assets/people.csv')[0][0]
    'J'
    """
    try:
        csv_data = reader(open(filepath))
    except FileNotFoundError as fileerr:
        log.error(str(fileerr))
        raise fileerr

    db = connect()
    people = []
    headers = ["name", "dept", "role", "email"]
    for line in csv_data:
        person_data = dict(zip(headers, [item.strip() for item in line]))
        pk = person_data.pop("email")
        person, created = add_person(db, pk, person_data)

        return_data = person.copy()
        return_data["created"] = created
        return_data["email"] = pk
        people.append(return_data)

    commit(db)
    return people
