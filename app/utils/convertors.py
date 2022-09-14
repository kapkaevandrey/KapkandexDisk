from datetime import datetime
from dateutil import tz


def convert_datetime_to_utc(
        date: datetime,
        timespec='seconds'
) -> str:
    """
    Convert
    date format -  2022-09-11T11:17:00+03:00 to
    UTC format - 2022-09-11T08:17:00.123456Z
    :param date: datetime
    :param timespec: str most have value 'seconds',
    'milliseconds' etc
    :return str (format like UTC time ISO8601)
    """
    utc_date = date.astimezone(tz.tzutc())
    date_str_with_tz = utc_date.isoformat(timespec=timespec)
    return date_str_with_tz[:-6] + 'Z'
