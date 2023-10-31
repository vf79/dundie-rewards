"""Initial

Revision ID: 2043b84bd5e5
Revises: 
Create Date: 2023-10-31 08:03:43.085505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '2043b84bd5e5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade. 2043b84bd5e5."""
    pass


def downgrade() -> None:
    """Downgrade. 2043b84bd5e5."""
    pass
