from datetime import datetime

import decimal

from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint, func, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base

class FundraiserProduct(Base):
    __tablename__ = "fundraiser_products"
    __table_args__ = (
        UniqueConstraint("fundraiser_id", "product_id", name="unique_fundraiser_product"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)

    fundraiser_id: Mapped[int] = mapped_column(
        ForeignKey("fundraisers.id"),
        nullable=False,
        index=True
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey("products.id"),
        nullable=False,
        index=True
    )

    sale_price: Mapped[decimal.Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    starting_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    ending_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )