from datetime import date, datetime
from typing import Optional

from sqlalchemy import Enum, Column, DateTime
from sqlmodel import SQLModel, Field


class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    name: str
    description: str

    create_at: datetime = Field(default_factory=datetime.now)
    modified_at: datetime = Field(
        sa_column=Column(DateTime, default=datetime.now,
                         onupdate=datetime.now, nullable=False)
    )
