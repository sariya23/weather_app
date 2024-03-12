from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

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


@router.post("/city", response_class=HTMLResponse)
def weather_city(request: Request, data: str = Form(...)) -> HTMLResponse:
    return template.TemplateResponse("weather_result.html", {"request": request, "city": data})

