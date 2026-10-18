CREATE TABLE IF NOT EXISTS historial (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    url    TEXT NOT NULL,
    fecha  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO historial (url, fecha)
SELECT url, fecha FROM (
    SELECT 'https://www.google.com'              AS url, '2026-10-10 09:00:00' AS fecha
    UNION ALL SELECT 'https://www.youtube.com',             '2026-10-10 09:15:00'
    UNION ALL SELECT 'https://github.com',                  '2026-10-11 10:30:00'
    UNION ALL SELECT 'https://www.wikipedia.org',           '2026-10-12 16:45:00'
    UNION ALL SELECT 'https://stackoverflow.com',           '2026-10-13 11:20:00'
    UNION ALL SELECT 'https://www.utectulancingo.edu.mx',   '2026-10-14 08:05:00'
    UNION ALL SELECT 'https://www.python.org',              '2026-10-15 19:10:00'
    UNION ALL SELECT 'https://flask.palletsprojects.com',   '2026-10-16 20:00:00'
)
WHERE NOT EXISTS (SELECT 1 FROM historial);