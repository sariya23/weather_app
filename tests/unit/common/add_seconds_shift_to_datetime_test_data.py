from datetime import datetime, timedelta


_datetime1 = datetime(year=1, month=1, day=1, hour=23)
_datetime2 = datetime(year=1, month=1, day=1, hour=0)
_datetime3 = datetime(year=2024, month=3, day=13)

_datetime1_shift =  _datetime1 + timedelta(seconds=3600)
_datetime2_shift = _datetime2 + timedelta(seconds=7200)
_datetime3_shift = _datetime3 + timedelta(seconds=-3600)

POSTITVE_DATETIME_SHIFT = (
    [_datetime1, 3600, _datetime1_shift.date(), _datetime1_shift.time()],
    [_datetime2, 7200, _datetime2_shift.date(), _datetime2_shift.time()],
    [_datetime3, -3600, _datetime3_shift.date(), _datetime3_shift.time()],
)
