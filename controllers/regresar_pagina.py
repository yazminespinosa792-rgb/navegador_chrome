from flask import Blueprint, redirect, url_for, flash
from controllers.conexion import obtener_conexion

bp = Blueprint("regresar_pagina", __name__)


@bp.post("/regresar")
def regresar():
    conn = obtener_conexion()
    try:
        paginas = conn.execute(
            "SELECT id, url FROM historial ORDER BY id DESC LIMIT 2"
        ).fetchall()

        if len(paginas) < 2:
            flash("No hay una página anterior a la cual regresar.", "error")
        else:
            actual, anterior = paginas[0], paginas[1]
            # POP: se quita el tope (LIFO) y la anterior pasa a ser la actual
            conn.execute("DELETE FROM historial WHERE id = ?", (actual["id"],))
            conn.commit()
            flash(f"Regresaste a: {anterior['url']}", "ok")
    finally:
        conn.close()

    return redirect(url_for("index.index"))
