from fastapi import FastAPI
from api.routes import libros_routes, autores_routes, editoriales_routes, categorias_routes, usuarios_routes, prestamos_routes

app = FastAPI(
    title="API Sistema de Biblioteca",
    description="API REST para gestionar libros, autores, usuarios y préstamos",
    version="1.0.0"
)

app.include_router(libros_routes.router)
app.include_router(autores_routes.router)
app.include_router(editoriales_routes.router)
app.include_router(categorias_routes.router)
app.include_router(usuarios_routes.router)
app.include_router(prestamos_routes.router)