from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from home.router import router as router_info
from weather.router import router as router_weather

app = FastAPI(title="Weather App")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(router_info)
app.include_router(router_weather)