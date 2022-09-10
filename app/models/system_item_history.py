from app.models import SystemItemBase

from sqlalchemy import (
    Column, DateTime, ForeignKey,
    BigInteger, String
)


class SystemItemHistory(SystemItemBase):
    id = Column(
        BigInteger,
        primary_key=True
    )
    item_id = Column(
        ForeignKey('systemitem.id'),
        nullable=False, index=True
    )
    parent_id = Column(
        String,
        nullable=True
    )
    date = Column(
        DateTime(timezone=True),
        index=True
    )

    def __repr__(self):
        return (
            f'Type - "{self.type}" '
            f'size - {self.size} '
            f'last update {self.date}'
        )
