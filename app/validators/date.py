from datetime import datetime
from dateutil import tz, parser

from typing import Optional

from fastapi.exceptions import RequestValidationError


def parse_and_check_date(date: str) -> datetime:
    """
    function parse string to datetime in iso format
    and also check dateformat
    :param date: str
    :return: datetime object
    """
    try:
        date = parser.isoparse(date)
    except ValueError:
        raise RequestValidationError('Invalid date format')
    check_date_is_valid(date)
    return date


def check_date_is_valid(
        date: datetime, lower_date: Optional[datetime] = None
) -> None:
    """
    function compares date
    :param date: datetime object
    :param lower_date: datetime object
    :return: None
    """
    utc_date = date.astimezone(tz.tzutc())
    if lower_date is None:
        lower_date = datetime.now(tz.tzutc())
    if utc_date > lower_date:
        raise RequestValidationError(
            f'date in UTC cant be larger then '
            f'{lower_date}'
        )
