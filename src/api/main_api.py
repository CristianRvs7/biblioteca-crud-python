from fastapi import FastAPI
from api.routes import libros_routes

app = FastAPI(
    title="API Sistema de Biblioteca",
    description="API REST para gestionar libros, autores, usuarios y préstamos",
    version="1.0.0"
)

app.include_router(libros_routes.router)


@app.get("/")
def inicio():
    return {"mensaje": "API de Biblioteca funcionando correctamente"}