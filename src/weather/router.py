from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def weather_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather"})


@router.post("/", response_class=HTMLResponse)
def get_weather(request: Request, data: str = Form(...)) -> HTMLResponse:
    logging.info(request)
    return template.TemplateResponse("weather.html", {"request": request, "page_name": "weather", "result": data})
