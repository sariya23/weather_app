class APIError(Exception):
    pass

class CityNotFound(APIError):
    pass


class BadConnection(APIError):
    pass


class APIResponseError(APIError):
    pass


class WrongWeatherDescriprion(APIError):
    pass
