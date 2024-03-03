from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests  # type: ignore

import logging
from dataclasses import dataclass
from src.weather.config import API_KEY, BASE_URL


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
    temperature: str
    wind_speed: str
    descroption: str


def get_weather_by_city(city: str) -> Weather | dict[str, str]:
    try:
        response = requests.post(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric", "lang": "ru"})
        result_data = response.json()
        result = {
            "location": city,
            "temperature": result_data["main"]["temp"],
            "wind_speed": result_data["wind"]["speed"],
            "description": result_data["main"]["description"],
        }
        return Weather(**result)
    except Exception as e:
        raise e 
    


@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather"})


@router.post("/", response_class=HTMLResponse)
def get_weather(request: Request, data: str = Form(...)) -> HTMLResponse:
    logging.info(data)
    try:
        return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather", "result": data})
    except Exception:
        return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather"}) 
