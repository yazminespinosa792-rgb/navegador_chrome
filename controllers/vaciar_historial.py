from flask import Blueprint, redirect, url_for, flash
from controllers.conexion import obtener_conexion

bp = Blueprint("vaciar_historial", __name__)


@bp.post("/vaciar")
def vaciar():
    conn = obtener_conexion()
    try:
        total = conn.execute("SELECT COUNT(*) FROM historial").fetchone()[0]
        if total == 0:
            flash("El historial ya está vacío.", "error")
        else:
            conn.execute("DELETE FROM historial")
            conn.commit()
            flash(f"Historial eliminado ({total} páginas).", "ok")
    finally:
        conn.close()

    return redirect(url_for("index.index"))
