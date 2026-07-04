--Archivo para insertar datos de prueba en la base de datos
-- Autores ========================================================

INSERT INTO autores (nombre_autor, apellido_autor) VALUES ('Stephen', 'King'), ('Gabriel', 'Garcia Marquez'), ('Rick', 'Riordan'), ('J. K.', 'Rowling'), ('William', 'Shakespeare'), ('Miguel', 'De Cervantes');

-- Categorias =====================================================

INSERT INTO categorias (nombre_categoria) VALUES ('Novela'), ('Fantasia'), ('Ciencia Ficción'), ('Historia'), ('Programación'), ('Literatura Clasica');

-- Editoriales ====================================================

INSERT INTO editoriales (nombre_editorial) VALUES ('Planeta'), ('Penguin Random House'), ('Alfaguara'), ('Anaya');

-- Libros =========================================================

INSERT INTO libros (
    isbn,   
    titulo_libro,
    id_autor,
    id_categoria,
    id_editorial,
    anio_lanzamiento,
    existencias
)
VALUES
('9780307743657','The Shining',1,1,2,1977,5),
('9781501142970','It',1,1,2,1986,3),
('9780450417399','Carrie',1,1,2,1974,4),

('9780307474728','Cien Años de Soledad',2,1,3,1967,6),
('9780307389732','El Amor en los Tiempos del Cólera',2,1,3,1985,4),
('9781400034956','Crónica de una Muerte Anunciada',2,1,3,1981,5),

('9781423103349','El Ladrón del Rayo',3,2,1,2005,8),
('9781423101475','El Mar de los Monstruos',3,2,1,2006,6),
('9781423101482','La Maldición del Titán',3,2,1,2007,5),

('9780747532743','Harry Potter y la Piedra Filosofal',4,2,2,1997,10),
('9780747538493','Harry Potter y la Cámara Secreta',4,2,2,1998,8),
('9780439136365','Harry Potter y el Prisionero de Azkaban',4,2,2,1999,7),

('9780743477123','Hamlet',5,6,4,1603,5),
('9780743477109','Romeo y Julieta',5,6,4,1597,5),
('9780743477550','Macbeth',5,6,4,1606,4),

('9788491050291','Don Quijote de la Mancha',6,6,1,1605,7),
('9788420412146','Novelas Ejemplares',6,6,1,1613,3),
('9788420412153','La Galatea',6,6,1,1585,2);

--===========================================
-- PRUEBAS REALIZANDO JOIN
--===========================================

SELECT l.titulo_libro, a.nombre_autor, a.apellido_autor, c.nombre_categoria, e.nombre_editorial, l.existencias FROM libros l

JOIN autores a
ON l.id_autor = a.id_autor

JOIN categorias c
ON l.id_categoria = c.id_categoria

JOIN editoriales e
ON l.id_editorial = e.id_editorial;

SELECT l.titulo_libro AS "Libro", a.nombre_autor AS "Nombre del Autor", a.apellido_autor FROM libros l JOIN autores a ON l.id_autor = a.id_autor WHERE a.nombre_autor LIKE 'Gabriel' OR a.apellido_autor LIKE 'Garcia' OR a.apellido_autor LIKE 'Marquez';

SELECT l.titulo_libro AS "Libro", a.nombre_autor AS "Nombre del Autor", a.apellido_autor AS "Apellidos del autor", c.nombre_categoria AS "Categoria", l.existencias AS "Existencias" FROM libros l JOIN autores a ON l.id_autor = a.id_autor JOIN categorias c ON l.id_categoria = c.id_categoria WHERE l.existencias > 5 ORDER BY l.existencias DESC;

SELECT id_libro, titulo_libro FROM libros WHERE titulo_libro LIKE '%Shining';

UPDATE libros SET existencias = 15, anio_lanzamiento = 1978 WHERE id_libro = 1;