import re
import datetime as dt


DATE_ISO_ZULU_FORMAT_REGEX = (
    r'\d{4}-(0[1-9]|1[0-2])'
    r'-(0[1-9]|1[0-9]|2[0-9]|3[0-1])'
    r'T(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]'
    r'(\.\d{1,6}){0,1}(Z|([+-]\d{2}:[0-5][0-9]))'
)
FILE_URL_REGEX = r'^\/[a-z_0-9\/-]+[^\/]$'

DATE_ISO_ZULU_FORMAT_TEMPLATE = re.compile(DATE_ISO_ZULU_FORMAT_REGEX)
FILE_URL_TEMPLATE = re.compile(FILE_URL_REGEX)

STATISTIC_TIME_PERIOD = dt.timedelta(hours=24)
