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
    description: str


def get_weather_by_city(city: str, lang: str = "ru", units: str = "metric") -> Weather:
    try:
        response = requests.get(f"{BASE_URL}q={city}&appid={API_KEY}&lang={lang}&units={units}")
        result_data = response.json()
        logging.info(result_data)
        result = {
            "location": city,
            "temperature": result_data["main"]["temp"],
            "wind_speed": result_data["wind"]["speed"],
            "description": result_data["weather"][0]["description"],
        }
        return Weather(**result)
    except Exception as e:
        raise e 
    


@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather"})


@router.post("/", response_class=HTMLResponse)
def get_weather(request: Request, data: str = Form(...)) -> HTMLResponse:
    weather = get_weather_by_city(data)
    return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather", "result": weather})
 
