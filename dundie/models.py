"""Models Class."""
from datetime import datetime
from typing import Optional

from pydantic import condecimal, validator
from sqlmodel import Field, Relationship, SQLModel

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password


class InvalidEmailError(Exception):
    """Extends exceptions."""

    pass


class Person(SQLModel, table=True):
    """Person model class."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(nullable=False, index=True)
    name: str = Field(nullable=False)
    dept: str = Field(nullable=False, index=True)
    role: str = Field(nullable=False)
    currency: str = Field(default="USD")

    balance: "Balance" = Relationship(back_populates="person")
    movement: "Movement" = Relationship(back_populates="person")
    user: "User" = Relationship(back_populates="person")

    @validator("email")
    def validate_email(cls, v: str) -> str:
        """Validate email."""
        if not check_valid_email(v):
            raise InvalidEmailError(f"Invalid email for {v!r}")
        return v

    def __str__(self) -> str:
        """View formated person."""
        return f"{self.name} - {self.role}"


class Balance(SQLModel, table=True):
    """Balance model class."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(
        foreign_key="person.id", sa_column_kwargs={"unique": True}
    )
    value: condecimal(decimal_places=3) = Field(default=0)

    person: Person = Relationship(back_populates="balance")

    class Config:
        """Config subclass."""

        json_encoders = {Person: lambda p: p.pk}


class Movement(SQLModel, table=True):
    """Movement model class."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    actor: str = Field(nullable=False, index=True)
    value: condecimal(decimal_places=3) = Field(default=0)
    date: datetime = Field(default_factory=lambda: datetime.now())

    person: Person = Relationship(back_populates="movement")

    class Config:
        """Config subclass."""

        json_encoders = {Person: lambda p: p.pk}


class User(SQLModel, table=True):
    """User model class."""

    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    password: str = Field(default_factory=generate_simple_password)

    person: Person = Relationship(back_populates="user")

    class Config:
        """Config subclass."""

        json_encoders = {Person: lambda p: p.pk}
