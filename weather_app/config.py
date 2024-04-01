from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    weather_api: str
    url_get_by_city_name: str = "https://api.openweathermap.org/geo/1.0/direct?"
    url_get_by_coordinates: str = "https://api.openweathermap.org/data/2.5/weather?"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")



settings = Settings(_env_file='.env', _env_file_encoding='utf-8')