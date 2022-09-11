from datetime import datetime
from dateutil import tz


def convert_datetime_to_utc(
        date: datetime,
        timespec='milliseconds'
) -> str:
    """
    Convert
    date format -  2022-09-11T11:17:00+03:00 to
    UTC format - 2022-09-11T08:17:00.123456Z
    :return str (format like UTC time ISO8601)
    """
    utc_date = date.astimezone(tz.tzutc())
    date_str_with_tz = utc_date.isoformat(timespec='milliseconds')
    return date_str_with_tz[:-6] + 'Z'


