from __future__ import annotations

from sqlalchemy import (
    Column, DateTime, ForeignKey, CheckConstraint, String,
)
from sqlalchemy.orm import relationship

from app.models import SystemItemBase


class SystemItem(SystemItemBase):
    __tableargs__ = (
        CheckConstraint('id != parent_id', 'id_not_parent_id'),
        CheckConstraint('size > 0', 'size_must_be_positive')
    )

    id = Column(
        String, primary_key=True
    )
    parent_id = Column(
        String, ForeignKey('systemitem.id'),
        nullable=True
    )
    children = relationship(
        'SystemItem',
        cascade='all,delete', order_by='SystemItem.date'
    )
    history = relationship(
        'SystemItemHistory',
        cascade='all,delete', order_by='SystemItemHistory.date'
    )
    date = Column(DateTime(timezone=True))

    def __repr__(self):
        return (f'Type - "{self.type}" '
                f'size - {self.size}.')
