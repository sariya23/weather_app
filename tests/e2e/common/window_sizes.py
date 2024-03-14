ALL_WINDOW_SIZES = [
    (2560, 1440),
    (1920, 1200),
    (1920, 1080),
    (1680, 1050),
    (1600, 900),
    (1536, 864),
    (1366, 768),
    (1440, 900),
    (1280, 1024),
    (1280, 800),
    (1024, 768),
    (800, 600),
    (393, 873),
    (360, 800),
    (414, 896),
    (412, 915),
    (390, 844),
    (393, 851),
    (375, 812),
]
ALL_WINDOW_SIZES += [(height, width) for width, height in ALL_WINDOW_SIZES]

DESKTOP_WINDOW_SIZES = [(width, height) for width, height in ALL_WINDOW_SIZES if 1024 < width]

MOBILE_WINDOW_SIZES = [(width, height) for width, height in ALL_WINDOW_SIZES if 767 >= width]

TABLET_WINDOW_SIZES = [(width, height) for width, height in ALL_WINDOW_SIZES if 1024 >= width > 767]

COMMON_WINDOW_SIZES = [(1920, 1080), (1024, 768), (393, 873)]

