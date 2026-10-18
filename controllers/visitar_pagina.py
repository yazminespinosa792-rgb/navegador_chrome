from flask import Blueprint, request, redirect, url_for, flash
from controllers.conexion import obtener_conexion

bp = Blueprint("visitar_pagina", __name__)


@bp.post("/visitar")
def visitar():
    url = request.form.get("url", "").strip()

    if not url:
        flash("Escribe la dirección de una página web.", "error")
        return redirect(url_for("index.index"))

    conn = obtener_conexion()
    try:
        # PUSH: la nueva página queda en el tope de la pila
        conn.execute("INSERT INTO historial (url) VALUES (?)", (url,))
        conn.commit()
        flash(f"Visitando: {url}", "ok")
    finally:
        conn.close()

    return redirect(url_for("index.index"))
