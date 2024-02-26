from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from info.router import router as router_info


app = FastAPI(title="Weather App")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(router_info)