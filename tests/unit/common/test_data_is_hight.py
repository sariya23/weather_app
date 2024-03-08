from datetime import time


NIGHT_TIME_BOUNDARY = [
    time(hour=7, minute=59),
]

DAY_TIME_BOUNDARU = [
    time(hour=18, minute=59),
]

NIGHT_TIME = [time(hour=h) for h in (0, 1, 2, 3, 4, 5, 6, 7, 19, 20, 21, 22, 23)] + NIGHT_TIME_BOUNDARY
DAY_TIME = [time(hour=h) for h in range(8, 19)] + DAY_TIME_BOUNDARU
