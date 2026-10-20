# Simulador de Navegador Web

Aplicación web en Python (Flask) + SQLite, con arquitectura MVC, que simula la administración de las páginas que visita un usuario en un navegador web. El historial usa una estructura de datos tipo **PILA (LIFO)**: el último elemento registrado es el primero en recuperarse.

## ¿Qué hace el sistema?

1. Visitar una página web
2. Regresar a la página anterior
3. Mostrar la página actual
4. Mostrar el historial de páginas visitadas en orden descendente (desde la página en la que estamos)
5. Verificar si el historial está vacío o, en su caso, eliminar el historial
6. Salir del programa

## Estructura del proyecto

```
NAVEGADOR/
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── controllers/
│   ├── __init__.py
│   ├── conexion.py            
│   ├── utilidades.py           
│   ├── index.py                
│   ├── visitar_pagina.py      
│   ├── regresar_pagina.py     
│   ├── vaciar_historial.py    
│   └── salir.py               
├── sql/
│   ├── navegador.db
│   └── script.sql
└── views/
    ├── layout.html
    ├── index.html
    └── salir.html
```

## ¿Cómo funciona el MVC?

1. El usuario escribe una URL o presiona un botón en la **vista** (`views/index.html`).
2. El navegador manda la acción a una ruta (`/visitar`, `/regresar`, `/vaciar`), que ejecuta el **controlador** correspondiente.
3. El controlador ejecuta el SQL necesario contra `sql/navegador.db` (el **modelo**).
4. El controlador redirige a `/`, donde `controllers/index.py` vuelve a consultar el historial y se lo pasa a la vista.

## ¿Cómo funciona la pila (LIFO)?

```sql
CREATE TABLE IF NOT EXISTS historial (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    url    TEXT NOT NULL,
    fecha  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

Como el `id` siempre crece, la página con el `id` más grande es la última visitada: el **tope de la pila**.

| Operación | Consulta SQL |
|---|---|
| Visitar página (push) | `INSERT INTO historial (url) VALUES (?)` |
| Página actual (peek) | `SELECT ... ORDER BY id DESC LIMIT 1` |
| Regresar (pop) | `DELETE FROM historial WHERE id = <tope>`; la anterior pasa a ser la actual |
| Mostrar historial | `SELECT ... ORDER BY id DESC` |
| ¿Historial vacío? | Verdadero si `SELECT COUNT(*) FROM historial` es 0 |
| Eliminar historial | `DELETE FROM historial` |

> Si solo hay una página en el historial, no se puede regresar y el sistema avisa que no existe una página anterior.

## Cómo ejecutarlo

Necesita Python 3 instalado. Desde la carpeta del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate        
pip install -r requirements.txt
python3 app.py
```

Abre en tu navegador: http://127.0.0.1:5000

La primera vez que corres `app.py`, si `sql/navegador.db` no existe, el sistema la crea automáticamente usando `sql/script.sql`.

## Cómo subirlo a GitHub

```bash
cd NAVEGADOR
git init
git add .
git commit -m "Simulador de navegador web con pila LIFO (MVC)"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
git push -u origin main
```

## Posibles mejoras a futuro

- Botón "Adelante" (segunda pila para las páginas de las que se regresó).
- Validar el formato de la URL.
- Mostrar la hora en formato local.
