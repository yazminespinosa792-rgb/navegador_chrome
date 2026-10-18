from flask import Blueprint, render_template
from controllers.conexion import obtener_conexion

bp = Blueprint("index", __name__)


@bp.get("/")
def index():
    conn = obtener_conexion()
    try:
        # Historial en orden descendente: del tope de la pila (más reciente) hacia abajo
        historial = conn.execute(
            "SELECT id, url, fecha FROM historial ORDER BY id DESC"
        ).fetchall()
    finally:
        conn.close()

    actual = historial[0] if historial else None   # tope de la pila
    vacio = len(historial) == 0

    return render_template(
        "index.html",
        historial=historial,
        actual=actual,
        total=len(historial),
        vacio=vacio,
    )
