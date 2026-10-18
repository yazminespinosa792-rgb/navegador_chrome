from flask import Blueprint, render_template

bp = Blueprint("salir", __name__)


@bp.get("/salir")
def salir():
    return render_template("salir.html")
