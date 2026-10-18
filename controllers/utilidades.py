from controllers.conexion import obtener_conexion, SCRIPT_PATH


def crear_bd():
    """Crea sql/navegador.db y la tabla historial si todavía no existen."""
    conn = obtener_conexion()
    try:
        conn.executescript(SCRIPT_PATH.read_text(encoding="utf-8"))
        conn.commit()
    finally:
        conn.close()
