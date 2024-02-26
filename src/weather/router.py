from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="/weather",
    tags=["Weather"],
)

template = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_weather(request: Request) -> HTMLResponse:
    return template.TemplateResponse("base.html", {"request": request, "page_name": "weather"})