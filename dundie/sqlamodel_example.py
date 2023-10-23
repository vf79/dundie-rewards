"""SQLModel Example."""
from typing import Optional

from sqlmodel import (
    Field,
    Relationship,
    Session,
    SQLModel,
    create_engine,
    select,
)

# Base (declarative_base)
# BaseModel (pydantici)


class Person(SQLModel, table=True):
    """Person sqlmodel class table."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str

    balance: "Balance" = Relationship(back_populates="person")


class Balance(SQLModel, table=True):
    """Balance sqlmodel class table."""

    id: Optional[int] = Field(default=None, primary_key=True)
    value: int
    person_id: int = Field(foreign_key="person.id")

    person: Person = Relationship(back_populates="balance")


engine = create_engine("sqlite:///assets/dbsqlmodel.db", echo=False)

SQLModel.metadata.create_all(bind=engine)

with Session(engine) as session:
    # person = Person(name="Ana")
    # session.add(person)
    #
    # person = Person(name="Beatriz")
    # session.add(person)
    #
    # person = Person(name="Maria")
    # session.add(person)
    #
    # session.commit()
    #
    # sql = select(Person)  # .where(Person.name == "Ana")
    # results = session.exec(sql)
    # for person in results:
    #     balance = Balance(value=60, person=person)
    #     session.add(balance)
    #     print(person.name, person.balance)
    # session.commit()
    sql = select(Person, Balance).where(Balance.person_id == Person.id)
    print(sql)
    sql = select(Person, Balance).join(Balance, isouter=True)
    print(sql)
