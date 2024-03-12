from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging
from datetime import datetime

from src.weather.exceptions import (
    APIWaetherFailed,
    APIWeatherBadResponse,
    WrongWeatherDescriprion,
)
from src.weather.utils import add_seconds_shift_to_datetime, get_weater_icon_by_description
from src.weather.service import get_weather_by_city, coords_of_city, Weather


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")
        
    
@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("no_weather.html", {"request": request})


@router.post("/select_city", response_class=HTMLResponse)
def weather_city(request: Request, data: str = Form(...)) -> HTMLResponse:
    cities = coords_of_city(data)
    return template.TemplateResponse("choice_city.html", {"request": request, "cities": cities})


@router.post("/weather_by_city/")
def get_weather(request: Request, city: str = Form(...)) -> HTMLResponse:
    return template.TemplateResponse("weather_result.html", {"request": request, "city": city})


