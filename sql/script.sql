-- Historial del navegador = PILA (LIFO).
-- El id siempre crece: la página con el id MÁS GRANDE es la última visitada (tope de la pila).
CREATE TABLE IF NOT EXISTS historial (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    url    TEXT NOT NULL,
    fecha  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
