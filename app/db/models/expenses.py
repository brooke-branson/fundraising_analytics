from datetime import datetime

from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class Expenses(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    fundraiser_id: Mapped[int] = mapped_column(
        ForeignKey("fundraisers.id"),
        nullable=False,
        index=True
    )

    description: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    amount: Mapped[Decimal] = mapped_column(
        Numeric,
        nullable=False
    )

    category: Mapped[str] = mapped_column(
        String(200),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )