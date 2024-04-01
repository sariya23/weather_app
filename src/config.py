from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    weather_api: str
    url_get_by_city_name: str
    url_get_by_coordinates: str



settings = Settings(_env_file='.env', _env_file_encoding='utf-8')
