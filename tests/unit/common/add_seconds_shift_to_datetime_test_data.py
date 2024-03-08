from datetime import datetime


_DATETIMES = (
    datetime(year=1, month=1, day=23, hour=23),
    datetime(year=1, month=1, day=23, hour=0),
    datetime(year=1, month=1, day=23, hour=15),
)

_SHIFT = [i for i in range(0, 86401, 3600)]
