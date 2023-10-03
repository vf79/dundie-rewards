"""Models Class"""
import json
from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal

from dundie.database import connect
from dundie.utils.email import check_valid_email


class InvalidEmailError(Exception):
    """Extends exceptions."""

    ...


class Serializable(ABC):
    """Serializable class."""

    def dict(self):
        """Return dict representation."""
        return vars(self)


@dataclass
class Person(Serializable):
    """Person Object."""

    pk: str
    name: str
    dept: str
    role: str

    def __post_init__(self):
        """Validate values."""
        if not check_valid_email(self.pk):
            raise InvalidEmailError(
                f"Email is invalid for {self} - {self.pk!r}"
            )

    def __str__(self):
        """Return string representation."""
        return f"{self.name} - {self.role}"


@dataclass
class Balance(Serializable):
    """Balance Object."""

    person: Person
    value: Decimal

    def dict(self):
        """Overwrite method dict."""
        return {"person": self.person.pk, "balance": str(self.value)}


@dataclass
class Movement(Serializable):
    """Movement Object."""

    person: Person
    date: datetime
    actor: str
    value: Decimal

    # def dict(self):
    #    return {
    #        Definir os valores para person, date
    #        actor e value
    #    }


db = connect()

for pk, data in db["people"].items():
    p = Person(pk, **data)


print(p)
# print(json.dumps(vars(p)))
print(json.dumps(p.dict()))

balance = Balance(person=p, value=Decimal(100))
# print(json.dumps(vars(balance)))
print(json.dumps(balance.dict()))


""" Json serialize
#int, float,
# bool True -> true
# None -> null
#{'key'} -> {"Key"}
# [], () -> []"""
