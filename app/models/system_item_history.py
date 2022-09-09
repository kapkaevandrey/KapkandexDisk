from app.models import SystemItemBase

from sqlalchemy import (
    Column, ForeignKey,
    BigInteger, String
)


class SystemItemHistory(SystemItemBase):
    id = Column(BigInteger, primary_key=True)
    item_id = Column(ForeignKey('systemitem.id'), nullable=False)
    parent_id = Column(String, nullable=True)

    def __repr__(self):
        return (
            f'Type - "{self.type}" '
            f'size - {self.size} '
            f'last update {self.date}'
        )
