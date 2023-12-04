-- Crear la tabla de proveedores
CREATE TABLE proveedores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    detalles VARCHAR(255),
    direccion VARCHAR(255),
    api_endpoint VARCHAR(255),
    props JSON,
    habilitado BOOLEAN
);

-- Insertar datos en la tabla de proveedores
INSERT INTO proveedores (nombre, detalles, direccion, api_endpoint, props, habilitado)
VALUES
    ('Tier 3 Proveedor de Plástico y Cartón', 'Detalles del proveedor', 'Dirección del proveedor', 'http://api.proveedor.com', '{"key": "value1"}', 1);

-- Crear la tabla de materia prima
CREATE TABLE materia_prima (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    props JSON,
    stock INT,
    habilitado BOOLEAN
);

-- Insertar datos en la tabla de materia prima
INSERT INTO materia_prima (nombre, descripcion, props, stock, habilitado)
VALUES
    ('Plástico', 'Material para la fabricación de piezas plásticas', '{"key": "value1"}', 1000, 1),
    ('Cartón', 'Material para empaques', '{"key": "value2"}', 500, 1);

-- Crear la tabla de piezas plásticas
CREATE TABLE piezas_plasticas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    props JSON,
    stock INT,
    habilitado BOOLEAN
);

-- Insertar datos en la tabla de piezas plásticas
INSERT INTO piezas_plasticas (nombre, descripcion, props, stock, habilitado)
VALUES
    ('Carcasas para celular', 'Carcasas de plástico para teléfonos celulares', '{"key": "value1"}', 200, 1),
    ('Airpods plastic box cover', 'Cubierta de plástico para caja de Airpods', '{"key": "value2"}', 150, 1),
    ('Airpods plastic cover', 'Cubierta de plástico para Airpods', '{"key": "value3"}', 100, 1);

-- Crear la tabla de solicitudes
CREATE TABLE solicitudes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tier VARCHAR(255),  
    carcasas INT,  
    plasticbox INT,
    plasticcover INT,
    estatus ENUM('pendiente', 'enviada', 'aceptada') DEFAULT 'pendiente',
    fecha_solicitud TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_envio TIMESTAMP NULL DEFAULT NULL,
    props JSON,
    habilitado BOOLEAN
);




-- Crear un trigger para establecer fecha_envio con la fecha actual al insertar un nuevo registro
DELIMITER //
CREATE TRIGGER before_insert_solicitudes
BEFORE INSERT ON solicitudes
FOR EACH ROW
SET NEW.fecha_envio = IF(NEW.estatus = 'enviada', CURRENT_TIMESTAMP, NULL);
//
DELIMITER ;

-- Insertar datos en la tabla de solicitudes
INSERT INTO solicitudes (tier, carcasas, plasticbox, plasticcover, fecha_solicitud, props, habilitado)
VALUES
    ('Tier 1 Equipos', 50, 30, 0, '2023-01-15', '{"key": "value1"}', 1);

-- Crear la tabla de envíos
CREATE TABLE envios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    solicitud_id INT,
    fecha_envio TIMESTAMP,
    cantidad_enviada INT,
    props JSON,
    habilitado BOOLEAN,
    FOREIGN KEY (solicitud_id) REFERENCES solicitudes(id)
);

-- Trigger para realizar registro en tabla de envíos al marcar una solicitud como enviada
DELIMITER //
CREATE TRIGGER after_solicitud_enviada_trigger
AFTER UPDATE ON solicitudes FOR EACH ROW
BEGIN
    IF NEW.estatus = 'enviada' AND OLD.estatus = 'pendiente' THEN
        INSERT INTO envios (solicitud_id, fecha_envio, cantidad_enviada, props, habilitado)
        VALUES (NEW.id, NOW(), NEW.carcasas + NEW.plasticbox + NEW.plasticcover, '{"key": "value1"}', 1);
    END IF;
END //
DELIMITER ;

-- Crear la tabla de recepciones
CREATE TABLE recepciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    materia_prima_id INT,
    fecha_recepcion TIMESTAMP,
    cantidad_recibida INT,
    props JSON,
    habilitado BOOLEAN,
    FOREIGN KEY (materia_prima_id) REFERENCES materia_prima(id)
);

-- Trigger para realizar registro en tabla de recepciones al insertar materia prima
DELIMITER //
CREATE TRIGGER after_materia_prima_insert_trigger
AFTER INSERT ON materia_prima FOR EACH ROW
BEGIN
    INSERT INTO recepciones (materia_prima_id, fecha_recepcion, cantidad_recibida, props, habilitado)
    VALUES (NEW.id, NOW(), NEW.stock, '{"key": "value1"}', 1);
END //
DELIMITER ;
