-- ======================================
-- ELIMINAR TABLAS EXISTENTES
-- ======================================

DROP TABLE IF EXISTS prestamos;
DROP TABLE IF EXISTS libros;
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS editoriales;
DROP TABLE IF EXISTS categorias;
DROP TABLE IF EXISTS autores;

-- ================================================================================
--  Creacion de tablas de la base de datos, integrando Foreign Keys
-- ================================================================================

CREATE TABLE autores(
    id_autor INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_autor VARCHAR(50) NOT NULL,
    apellido_autor VARCHAR(50) NOT NULL
);

CREATE TABLE categorias(
    id_categoria INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_categoria VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE editoriales(
    id_editorial INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombre_editorial VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE libros(
    id_libro INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    isbn CHAR(13) NOT NULL UNIQUE,
    titulo_libro VARCHAR(150) NOT NULL,
    id_autor INTEGER NOT NULL,
    id_categoria INTEGER NOT NULL,
    id_editorial INTEGER NOT NULL,
    anio_lanzamiento INTEGER NOT NULL,
    existencias INTEGER NOT NULL CHECK (existencias >= 0),

-- ================= Relaciones con otras tablas ==============================

    FOREIGN KEY(id_autor) REFERENCES autores(id_autor) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_categoria) REFERENCES categorias(id_categoria) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_editorial) REFERENCES editoriales(id_editorial) ON DELETE RESTRICT ON UPDATE CASCADE
);

CREATE TABLE usuarios(
    id_usuario INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nombres_usuario VARCHAR (50) NOT NULL,
    apellidos_usuario VARCHAR(50) NOT NULL,
    docidentificacion VARCHAR(20) NOT NULL UNIQUE,
    correo_usuario VARCHAR(100) NOT NULL UNIQUE,
    contacto_usuario VARCHAR(20) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE prestamos(
    id_prestamo INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    id_libro INTEGER NOT NULL,
    fecha_prestamo TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_limite TIMESTAMP NOT NULL,
    fecha_devolucion TIMESTAMP,
    estado VARCHAR(20),

    -- ================= Relaciones con otras tablas ==============================
    FOREIGN KEY(id_usuario) REFERENCES usuarios(id_usuario) ON DELETE RESTRICT ON UPDATE CASCADE,
    FOREIGN KEY(id_libro) REFERENCES libros(id_libro) ON DELETE RESTRICT ON UPDATE CASCADE
    );