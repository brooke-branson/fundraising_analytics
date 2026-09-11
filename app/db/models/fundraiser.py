from datetime import date, datetime

from sqlalchemy import Date, DateTime, ForeignKey, Integer, UniqueConstraint, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Fundraiser(Base):
    """
    Fundraiser Schema:

    id: int -> Primary Key

    organization_id: int -> Foreign Key, ID of Organization holding event
    name: str -> Name of the event "Bake Sale"
    event_type: str -> What type of event "Food sale, craft sale, etc..."
    event_date: date -> Scheduled date of event (date(year, mm, dd))
    expected_attendance: int -> Expected attendance number (required)
    actual_attendance (Optional at insert): int -> Actual. Not required at insert
    status: str -> scheduled/completed/in-prog

    created_at: DateTime object, created at insert.
    
    """
    __tablename__ = "fundraisers"
    __table_args__ = (
        UniqueConstraint("organization_id", "name", "event_date", name="unique_scheduled_fundraiser"),
    )
    id: Mapped[int] = mapped_column(primary_key=True)

    organization_id: Mapped[int] = mapped_column(
        ForeignKey("organizations.id"),
        nullable=False,
        index=True,
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    event_type: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    event_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    expected_attendance: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    actual_attendance: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="planning",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )