from flask import Flask

from controllers.utilidades import crear_bd
from controllers.index import bp as index_bp
from controllers.visitar_pagina import bp as visitar_bp
from controllers.regresar_pagina import bp as regresar_bp
from controllers.vaciar_historial import bp as vaciar_bp
from controllers.salir import bp as salir_bp

app = Flask(__name__, template_folder="views")
app.secret_key = "cambia-esta-clave"   # necesaria para flash()

crear_bd()

app.register_blueprint(index_bp)
app.register_blueprint(visitar_bp)
app.register_blueprint(regresar_bp)
app.register_blueprint(vaciar_bp)
app.register_blueprint(salir_bp)

if __name__ == "__main__":
    app.run(debug=True)
