"""SQLAlchemy example."""
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    create_engine,
    select,
)
from sqlalchemy.orm import DeclarativeBase, Session, relationship


class Base(DeclarativeBase):
    """Base class."""

    pass


class Person(Base):
    """Person Table."""

    __tablename__ = "person"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    def __repr__(self) -> str:
        """Print formated string."""
        return f"Person(id={self.id!r}, name={self.name!r})"


class Balance(Base):
    """Balance Table."""

    __tablename__ = "balance"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    value = Column(Integer, nullable=False)

    person_id = Column(Integer, ForeignKey(Person.id))

    person = relationship("Person", foreign_keys="Balance.person_id")

    def __repr__(self) -> str:
        """Print formated string."""
        return f"Balance(id={self.id!r},\
        name={self.person.name!r},\
        value={self.value!r})"


engine = create_engine("sqlite:///assets/database.db", echo=False)

Base.metadata.create_all(bind=engine)

# Person Example
# with Session(engine) as session:
#    person = Person(name="Teste")
#    session.add(person)
#    session.commit()

# session = Session(engine)
# stmt = select(Person).where(Person.name.in_(["Valmir", "Teste"]))

# for person in session.scalars(stmt):
#    print(person)

# Balance Example
with Session(engine) as session:
    # balance = Balance(value=40, person_id=2)
    # session.add(balance)
    # balance = Balance(value=40, person_id=1)
    # session.add(balance)
    # session.commit()

    stmt = select(Balance)
    result = session.execute(stmt)
    for row in result:
        print(row.index(1))
