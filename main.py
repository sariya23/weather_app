from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()
app.mount("/static", StaticFiles(directory="static/"), name="static")
templates = Jinja2Templates(directory='templates') 

@app.get("/", response_model=HTMLResponse)
def hello_api(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"id": id} 
    )
