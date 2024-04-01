from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix="",
    tags=["Home"],
)

template = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def get_home_page(request: Request) -> HTMLResponse:
    return template.TemplateResponse("home.html", {"request": request, "page_name": "info"})