class APIError(Exception):
    pass

class WrongCityName(APIError):
    pass


class APIWaetherFailed(APIError):
    pass


class APIWeatherBadResponse(APIError):
    pass


class WrongWeatherDescriprion(APIError):
    pass
