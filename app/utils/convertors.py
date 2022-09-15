import datetime as dt


def convert_datetime_to_utc(
        date: dt.datetime,
        timespec='seconds'
) -> str:
    """
    Convert
    date format -  2022-09-11T11:17:00+00:00 to
    UTC format - 2022-09-11T11:17:00Z
    :param date: datetime
    :param timespec: str most have value 'seconds',
    'milliseconds' etc
    :return str (format like UTC time ISO8601)
    """
    date_str_with_tz = date.isoformat(timespec=timespec)
    if date.utcoffset() is None:
        return date_str_with_tz + 'Z'
    if date.utcoffset() == dt.timedelta():
        return date_str_with_tz[:-6] + 'Z'
    return date_str_with_tz
