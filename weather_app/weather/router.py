from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import logging
from datetime import datetime

from weather_app.weather.utils import (
    add_seconds_shift_to_datetime,
    get_weater_icon_by_description,
)
from weather_app.weather.service import (
    get_weather_by_coordinates,
    get_city_locations_with_same_name,
    Coordinates,
)
from weather_app.weather.exceptions import (
    CityNotFound,
    BadConnection,
    APIResponseError,
)

logging.basicConfig(
    level=logging.INFO,
    filename="py_log.log",
    filemode="w",
    format="%(asctime)s %(levelname)s %(message)s",
)

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("no_weather.html", {"request": request})


@router.post("/select_city/", response_class=HTMLResponse)
def select_city(request: Request, city_name: str = Form(...)) -> HTMLResponse:
    try:
        cities = get_city_locations_with_same_name(city_name)
        return template.TemplateResponse(
            "choice_city.html", {"request": request, "cities": cities}
        )
    except CityNotFound as e:
        logging.error(f"EXP {str(e)}\n, request: {request}\n, coords: {city_name}")
        return template.TemplateResponse(
            "error.html", {"request": request, "message": "Такого города нет"}
        )
    except Exception as e:
        logging.error(f"EXP {str(e)}\n, request: {request}\n, coords: {city_name}")
        return template.TemplateResponse(
            "error.html", {"request": request, "message": "Все сломалось"}
        )



@router.post("/weather_by_city/")
def get_weather(request: Request, coords: str = Form(...)) -> HTMLResponse: 
    try:
        coordinates = Coordinates(*coords.split())
        weather = get_weather_by_coordinates(coordinates)
        now_datetime_utc = datetime.utcnow()
        date, time = add_seconds_shift_to_datetime(now_datetime_utc, weather.UTC_shift)
        weather_icon_path = get_weater_icon_by_description(weather.description, time)
        formatted_date = date.strftime("%d.%m.%Y")
        formatted_time = time.strftime("%H:%M")
        return template.TemplateResponse(
            "weather_result.html",
            {
                "request": request,
                "weather": weather,
                "date": formatted_date,
                "time": formatted_time,
                "icon": weather_icon_path,
                "UTC_shift": f"{(weather.UTC_shift / 3600):+g}"
            },
        )
    except BadConnection as e:
        logging.error(f"Exception {str(e)}\n, request: {request}\n, coords: {coords}")
        return template.TemplateResponse(
            "error.html", {"request": request, "message": "Проблемы с соединением"}
        )
    except APIResponseError as e:
        logging.error(f"Exception {str(e)}\n, request: {request}\n, coords: {coords}")
    except Exception as e:
        logging.error(f"EXP {str(e)}\n, request: {request}\n, coords: {coords}")
        return template.TemplateResponse(
            "error.html", {"request": request, "message": "Все сломалось"}
        )
