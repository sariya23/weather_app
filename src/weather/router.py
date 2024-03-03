from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests  # type: ignore

import logging
import math

from dataclasses import dataclass
from src.weather.config import API_KEY, BASE_URL
from src.weather.exceptions import (
    APIWaetherFailed,
    APIWeatherBadResponse,
)


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")

@dataclass(frozen=True, slots=True)
class Weather:
    location: str
    temperature: int
    wind_speed: str
    description: str


def get_weather_by_city(city: str, lang: str = "ru", units: str = "metric") -> Weather:
    try:
        response = requests.get(f"{BASE_URL}q={city}&appid={API_KEY}&lang={lang}&units={units}")
        result_data = response.json()
        result = {
            "location": city,
            "temperature": math.ceil((result_data["main"]["temp"])),
            "wind_speed": result_data["wind"]["speed"],
            "description": result_data["weather"][0]["description"],
        }
        return Weather(**result)

    except requests.exceptions.RequestException:
        raise APIWaetherFailed

    except KeyError:
        raise APIWeatherBadResponse
        
    
@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("weather.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
def get_weather(request: Request, data: str = Form(...)) -> HTMLResponse:
    try:
        weather = get_weather_by_city(data)
        return template.TemplateResponse("weather.html", {"request": request, "result": weather})
    except APIWeatherBadResponse:
        message = "Что-то пошло не так, проверьте правильность написания города."
        return template.TemplateResponse("weather.html", {"request": request, "message": message})
    except APIWaetherFailed:
        message = "Ошибка стороннего сервиса"
        return template.TemplateResponse("weather.html", {"request": request, "message": message})
    except Exception as e:
        message = "Все сломалось, простите :("
        logging.error(e)
        return template.TemplateResponse("weather.html", {"request": request, "message": message})


 
