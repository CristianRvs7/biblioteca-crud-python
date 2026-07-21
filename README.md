# 📚 Sistema de Gestión de Biblioteca

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

## Descripción

Sistema backend para la gestión de una biblioteca, desarrollado con **Python, FastAPI y PostgreSQL**.

El proyecto permite administrar libros, autores, categorías, editoriales, usuarios y préstamos mediante operaciones CRUD, consultas SQL, validación de datos y reglas de negocio relacionadas con el control de existencias.

El sistema comenzó como una aplicación de consola y posteriormente fue reorganizado y migrado a una **API REST con FastAPI**, manteniendo la lógica y la base de datos de la primera versión.

Actualmente, la API representa la implementación principal del proyecto.

---

## Evolución del proyecto

### Primera etapa: aplicación de consola

La primera versión del sistema funcionaba mediante una interfaz de línea de comandos.

Se desarrollaron menús interactivos para gestionar:

- Libros.
- Autores.
- Categorías.
- Editoriales.
- Usuarios.
- Préstamos.

Durante esta etapa se implementaron:

- Operaciones CRUD.
- Conexión entre Python y PostgreSQL.
- Consultas SQL directas.
- Relaciones entre tablas.
- Búsquedas y filtros.
- Validaciones de entrada.
- Control de préstamos y devoluciones.
- Separación del proyecto por módulos.

Esta primera versión permitió construir la lógica principal del sistema antes de exponerla mediante una API.

### Segunda etapa: migración a una API REST

Después de completar la aplicación de consola, el proyecto fue migrado a una API REST utilizando FastAPI.

Durante esta etapa se incorporaron:

- Endpoints HTTP para cada entidad.
- Rutas separadas por recurso.
- Esquemas de validación con Pydantic.
- Códigos de estado HTTP.
- Manejo de errores mediante `HTTPException`.
- Documentación interactiva con Swagger UI.
- Validación de correos electrónicos.
- Respuestas en formato JSON.
- Consultas relacionadas mediante `JOIN`.
- Reutilización de los repositorios y modelos existentes.

La migración permitió transformar una aplicación local en un servicio backend que puede ser consumido por una aplicación web, móvil u otro cliente.

---

## Funcionalidades actuales de la API

### Libros

- Crear libros.
- Listar libros.
- Consultar un libro por ID.
- Actualizar libros.
- Eliminar libros.
- Mostrar información del autor, categoría y editorial mediante relaciones.
- Consultar las existencias disponibles.

### Autores

- Crear autores.
- Listar autores.
- Consultar un autor por ID.
- Actualizar autores.
- Eliminar autores.

### Categorías

- Crear categorías.
- Listar categorías.
- Consultar una categoría por ID.
- Actualizar categorías.
- Eliminar categorías.

### Editoriales

- Crear editoriales.
- Listar editoriales.
- Consultar una editorial por ID.
- Actualizar editoriales.
- Eliminar editoriales.

### Usuarios

- Crear usuarios.
- Listar usuarios.
- Consultar un usuario por ID.
- Actualizar usuarios.
- Eliminar usuarios.
- Validar el formato del correo electrónico.

### Préstamos

- Registrar préstamos.
- Listar préstamos.
- Consultar un préstamo por ID.
- Actualizar préstamos.
- Registrar devoluciones.
- Eliminar préstamos.
- Mostrar el nombre del usuario y el título del libro mediante relaciones.
- Controlar automáticamente las existencias de los libros.

---

## Reglas de negocio implementadas

El módulo de préstamos incluye reglas de negocio para mantener la consistencia de la información:

- Verificar que el usuario exista antes de registrar un préstamo.
- Verificar que el libro exista.
- Comprobar que el libro tenga existencias disponibles.
- Reducir una existencia al registrar un préstamo.
- Registrar inicialmente el préstamo con estado `Activo`.
- Permitir actualizar la fecha límite, la fecha de devolución y el estado.
- Recuperar una existencia cuando se devuelve o elimina un préstamo.
- Consultar información relacionada del usuario y del libro.
- Evitar que las existencias de un libro sean negativas.

---

## Tecnologías utilizadas

### Backend

- Python 3.
- FastAPI.
- Pydantic.
- Uvicorn.

### Base de datos

- PostgreSQL.
- Psycopg.
- SQL.
- Consultas con `JOIN`.
- Claves primarias y foráneas.

### Herramientas

- Git.
- GitHub.
- Visual Studio Code.
- Swagger UI.
- ReDoc.

---

## Arquitectura del proyecto

El proyecto está organizado separando las responsabilidades principales:

```text
Solicitud HTTP
      ↓
Router de FastAPI
      ↓
Schema de Pydantic
      ↓
Repositorio
      ↓
PostgreSQL
```

### Responsabilidades

- **Routes:** reciben las solicitudes HTTP y devuelven las respuestas.
- **Schemas:** validan los datos enviados a la API.
- **Repositories:** contienen las consultas y operaciones con PostgreSQL.
- **Models:** representan las entidades del sistema.
- **Database:** administra la configuración y conexión con la base de datos.
- **Menus:** contiene la interfaz de consola desarrollada en la primera etapa.

---

## Estructura del proyecto

```text
BibliotecaCRUD/
│
├── docs/
│   └── DiagramaDB.png
│
├── src/
│   ├── api/
│   │   ├── main_api.py
│   │   │
│   │   ├── routes/
│   │   │   ├── autores_routes.py
│   │   │   ├── categorias_routes.py
│   │   │   ├── editoriales_routes.py
│   │   │   ├── libros_routes.py
│   │   │   ├── prestamos_routes.py
│   │   │   └── usuarios_routes.py
│   │   │
│   │   └── schemas/
│   │       ├── autor_schema.py
│   │       ├── categoria_schema.py
│   │       ├── editorial_schema.py
│   │       ├── libro_schema.py
│   │       ├── prestamo_schema.py
│   │       └── usuario_schema.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── config.py
│   │   ├── schema.sql
│   │   └── seed.sql
│   │
│   ├── menus/
│   │   └── ...
│   │
│   ├── models/
│   │   ├── autor.py
│   │   ├── categoria.py
│   │   ├── editorial.py
│   │   ├── libro.py
│   │   ├── prestamo.py
│   │   └── usuario.py
│   │
│   ├── repositories/
│   │   ├── autor_repository.py
│   │   ├── categoria_repository.py
│   │   ├── editorial_repository.py
│   │   ├── libro_repository.py
│   │   ├── prestamo_repository.py
│   │   └── usuario_repository.py
│   │
│   └── utils/
│       └── validaciones.py
│
├── README.md
└── requirements.txt
```

---

## Endpoints principales

La API contiene rutas para los siguientes recursos:

| Recurso | Ruta base |
|---|---|
| Libros | `/libros` |
| Autores | `/autores` |
| Categorías | `/categorias` |
| Editoriales | `/editoriales` |
| Usuarios | `/usuarios` |
| Préstamos | `/prestamos` |

Cada recurso implementa operaciones CRUD mediante los siguientes métodos HTTP:

| Método | Operación |
|---|---|
| `GET` | Listar registros o consultar uno por ID |
| `POST` | Crear un nuevo registro |
| `PUT` | Actualizar un registro existente |
| `DELETE` | Eliminar un registro |

Ejemplos:

```http
GET /libros
GET /libros/1
POST /libros
PUT /libros/1
DELETE /libros/1
```

---

## Base de datos

El proyecto utiliza PostgreSQL como sistema gestor de bases de datos.

Las principales tablas son:

- Autores.
- Categorías.
- Editoriales.
- Libros.
- Usuarios.
- Préstamos.

Las relaciones se implementan mediante claves foráneas para garantizar la integridad referencial.

Un libro está relacionado con:

- Un autor.
- Una categoría.
- Una editorial.

Un préstamo está relacionado con:

- Un usuario.
- Un libro.

---

## Diagrama de la base de datos

![Diagrama de la base de datos](docs/DiagramaDB.png)

---

## Requisitos

Antes de ejecutar el proyecto es necesario tener instalado:

- Python 3.14 o una versión compatible.
- PostgreSQL.
- FastAPI.
- Uvicorn.
- Psycopg.
- Las dependencias incluidas en `requirements.txt`.

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/CristianRvs7/biblioteca-crud-python.git
```

### 2. Entrar en el proyecto

```bash
cd biblioteca-crud-python
```

### 3. Crear un entorno virtual

```bash
python -m venv .venv
```

En Windows:

```bash
.venv\Scripts\activate
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar PostgreSQL

Configura los datos de conexión en:

```text
src/database/config.py
```

La configuración debe incluir los datos correspondientes a tu instalación de PostgreSQL:

- Nombre de la base de datos.
- Usuario.
- Contraseña.
- Host.
- Puerto.

### 6. Crear las tablas

Ejecuta el contenido de:

```text
src/database/schema.sql
```

Opcionalmente, puedes insertar datos de prueba ejecutando:

```text
src/database/seed.sql
```

---

## Ejecutar la API

Desde la carpeta raíz del proyecto, entra en `src`:

```bash
cd src
```

Inicia el servidor de desarrollo:

```bash
py -m uvicorn api.main_api:app --reload
```

También puedes utilizar:

```bash
python -m uvicorn api.main_api:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

---

## Documentación de la API

FastAPI genera automáticamente documentación interactiva para probar los endpoints.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Desde Swagger UI es posible:

- Consultar los endpoints disponibles.
- Revisar los datos requeridos.
- Enviar solicitudes.
- Observar las respuestas de la API.
- Comprobar los códigos de estado HTTP.

---

## Objetivos de aprendizaje

Este proyecto fue desarrollado para fortalecer conocimientos en:

- Python.
- Programación orientada a objetos.
- Desarrollo backend.
- Diseño de APIs REST.
- FastAPI.
- Pydantic.
- PostgreSQL.
- SQL.
- Operaciones CRUD.
- Relaciones entre tablas.
- Consultas con `JOIN`.
- Validación de datos.
- Manejo de errores HTTP.
- Arquitectura modular.
- Git y GitHub.
- Migración de una aplicación de consola a una API REST.

---

## Mejoras futuras

- Autenticación de usuarios.
- Autorización mediante roles.
- Implementación de JWT.
- Pruebas automatizadas con `pytest`.
- Variables de entorno para proteger la configuración.
- Contenerización con Docker.
- Historial de préstamos por usuario.
- Ranking de libros más prestados.
- Paginación y filtros en los endpoints.
- Interfaz web para consumir la API.
- Despliegue de la aplicación en un servicio en la nube.

---

## Autor

**Cristian Riquelmi Umaña Rivas**

Proyecto desarrollado como parte de mi proceso de formación en desarrollo backend con Python, FastAPI y PostgreSQL.