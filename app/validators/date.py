from datetime import datetime
from dateutil import tz, parser

from typing import Optional

from fastapi.exceptions import RequestValidationError


def parse_and_check_date(date: str) -> datetime:
    try:
        date = parser.isoparse(date)
    except ValueError:
        raise RequestValidationError('Invalid date format')
    check_date_is_valid(date)
    return date


def check_date_is_valid(
        date: datetime, lower_date: Optional[datetime] = None
) -> None:
    if lower_date is None:
        lower_date = datetime.now(tz.tzutc())
    if date > lower_date:
        raise RequestValidationError(
            f'date in UTC cant be larger then '
            f'{lower_date}'
        )
