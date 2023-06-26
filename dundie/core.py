"""Core module of dundie"""
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
        with open(filepath) as loadfile:
            return [line.strip() for line in loadfile.readlines()]
    except FileNotFoundError as fileerr:
        log.error(str(fileerr))
        raise fileerr