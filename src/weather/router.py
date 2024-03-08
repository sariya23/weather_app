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
from src.weather.service import get_weather_by_city
from src.weather.service import Weather


logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")
        
    
@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("weather.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
def get_weather(request: Request, data: str = Form(...)) -> HTMLResponse:
    try:
        weather: Weather = get_weather_by_city(data)
        now_datetime_utc = datetime.utcnow()
        date, time = add_seconds_shift_to_datetime(now_datetime_utc, weather.UTC_shift)
        weather_icon_path = get_weater_icon_by_description(weather.description, time)
        formatted_date = date.strftime("%d.%m.%Y")
        formatted_time = time.strftime("%H:%M")
        return template.TemplateResponse(
            "weather.html",
            {
                "request": request,
                "weather": weather,
                "date": formatted_date,
                "time": formatted_time,
                "icon": weather_icon_path,
            }
        )
    except APIWeatherBadResponse:
        message = "Что-то пошло не так, проверьте правильность написания города."
        return template.TemplateResponse("weather.html", {"request": request, "message": message})
    except APIWaetherFailed:
        message = "Ошибка стороннего сервиса"
        return template.TemplateResponse("weather.html", {"request": request, "message": message})
    except WrongWeatherDescriprion as e:
        logging.error(e)
        message = "Мы не учли все варианты погоды :("
        return template.TemplateResponse("weather.html", {"request": request, "message": message})
    except Exception as e:
        message = "Все сломалось, простите :("
        logging.error(e)
        return template.TemplateResponse("weather.html", {"request": request, "message": message})


 
