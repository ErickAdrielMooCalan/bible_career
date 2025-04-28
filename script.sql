-- Crear tabla sabados
CREATE TABLE IF NOT EXISTS sabados (
    id_sabado INTEGER PRIMARY KEY AUTOINCREMENT,
    mes INTEGER NOT NULL,           -- El mes (1-12)
    semana INTEGER NOT NULL,        -- El número de la semana (1-4)
    fecha DATE NOT NULL             -- Fecha del sábado
);

-- Crear tabla preguntas
CREATE TABLE IF NOT EXISTS preguntas (
    id_pregunta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sabado INTEGER NOT NULL,            -- Relacionado con la tabla sabados
    texto TEXT NOT NULL,                   -- El texto de la pregunta
    estado TEXT NOT NULL CHECK(estado IN ('disponible', 'respondida', 'anulada')),  -- Estado de la pregunta
    valor INTEGER NOT NULL DEFAULT 10,      -- Valor de la pregunta (generalmente 10 puntos)
    respuesta_correcta TEXT NOT NULL,      -- Respuesta correcta para la pregunta
    FOREIGN KEY (id_sabado) REFERENCES sabados(id_sabado)
);

-- Crear tabla grupos
CREATE TABLE IF NOT EXISTS grupos (
    id_grupo INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL                -- Nombre del grupo
);

-- Crear tabla respuestas
CREATE TABLE IF NOT EXISTS respuestas (
    id_respuesta INTEGER PRIMARY KEY AUTOINCREMENT,
    id_grupo INTEGER NOT NULL,           -- Relacionado con la tabla grupos
    id_pregunta INTEGER NOT NULL,        -- Relacionado con la tabla preguntas
    respuesta TEXT NOT NULL,             -- Respuesta dada por el grupo
    resultado TEXT NOT NULL CHECK(resultado IN ('correcta', 'incorrecta', 'robada')), -- Resultado de la respuesta
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo),
    FOREIGN KEY (id_pregunta) REFERENCES preguntas(id_pregunta)
);

-- Crear tabla puntajes
CREATE TABLE IF NOT EXISTS puntajes (
    id_grupo INTEGER PRIMARY KEY,           -- Relacionado con la tabla grupos
    puntaje_total INTEGER DEFAULT 0,        -- Puntaje total acumulado por el grupo
    FOREIGN KEY (id_grupo) REFERENCES grupos(id_grupo)
);