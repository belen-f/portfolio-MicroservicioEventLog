from fastapi import FastAPI
from routers import events
import os

app=FastAPI(
    title="Event Log",
    description="Microservicio para la gestión y registro de bitácoras de eventos",
    version="1.0.0"
) 
 

app.include_router(events.router)


@app.get("/", include_in_schema=False)
def read_root():
    return {"Hello World"}


# Url local: http://127.0.0.1:8000/url
# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc