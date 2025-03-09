BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS detalles_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_pedido INTEGER NOT NULL, 
            id_plato INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK (cantidad > 0), 
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE, 
            FOREIGN KEY (id_plato) REFERENCES platos(id) ON DELETE CASCADE
        );
CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_cliente TEXT NOT NULL, 
            id_restaurante INTEGER NOT NULL, 
            estado TEXT CHECK (estado IN ('pendiente', 'en preparación', 'en camino', 'entregado')), 
            FOREIGN KEY (id_cliente) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );
CREATE TABLE IF NOT EXISTS platos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            precio REAL NOT NULL CHECK (precio > 0), 
            descripcion TEXT NOT NULL,
            id_restaurante INTEGER NOT NULL, 
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );
CREATE TABLE IF NOT EXISTS repartidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nif TEXT UNIQUE NOT NULL, 
            nombre TEXT NOT NULL, 
            id_pedido_asignado INTEGER, 
            vehiculo TEXT, 
            FOREIGN KEY (id_pedido_asignado) REFERENCES pedidos(id) ON DELETE SET NULL
        );
CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            direccion TEXT NOT NULL, 
            categoria TEXT, 
            telefono TEXT UNIQUE,
            horario TEXT,
            calificacion REAL CHECK (calificacion >= 0 AND calificacion <= 5)
        );
CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            direccion TEXT, 
            telefono TEXT UNIQUE NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
INSERT INTO "detalles_pedido" ("id","id_pedido","id_plato","cantidad") VALUES (6,1,1,2),
 (7,2,2,1),
 (8,3,3,3),
 (9,4,4,1),
 (10,5,5,2),
 (11,6,6,2),
 (12,7,7,3),
 (13,8,8,1),
 (14,9,9,2),
 (15,10,10,3);
INSERT INTO "pedidos" ("id","id_cliente","id_restaurante","estado") VALUES (6,'1',1,'pendiente'),
 (7,'2',2,'en preparación'),
 (8,'3',3,'en camino'),
 (9,'4',4,'entregado'),
 (10,'5',5,'pendiente'),
 (11,'6',6,'en preparación'),
 (12,'7',7,'en camino'),
 (13,'8',8,'entregado'),
 (14,'9',9,'pendiente');
INSERT INTO "platos" ("id","nombre","precio","descripcion","id_restaurante") VALUES (11,'Pizza Margherita',8.5,'Pizza clásica con tomate, mozzarella y albahaca',1),
 (12,'Spaghetti Carbonara',10.0,'Spaghetti con salsa cremosa de huevo y panceta',1),
 (13,'Sushi Rolls',12.0,'Rollos de sushi con atún, salmón y aguacate',2),
 (14,'Sashimi de Salmón',15.0,'Salmón fresco en láminas finas',2),
 (15,'Tacos al Pastor',6.5,'Tacos de cerdo marinados con piña y cilantro',3),
 (16,'Burritos de Carne',7.0,'Burritos con carne, arroz, frijoles y salsa picante',3),
 (17,'Hamburguesa El Grill',9.0,'Hamburguesa de carne con queso cheddar, cebolla caramelizada',4),
 (18,'Hot Dog con Mostaza',4.5,'Perro caliente con mostaza, ketchup y cebolla',4),
 (19,'Ensalada Vegana',6.0,'Ensalada con quinoa, aguacate, zanahoria y tomate',5),
 (20,'Hamburguesa Vegana',7.5,'Hamburguesa con pan de avena y proteína vegetal',5),
 (21,'Bocadillo de Jamón',5.5,'Bocadillo con jamón serrano y tomate',6),
 (22,'Croquetas Caseras',4.0,'Croquetas de pollo y jamón',6),
 (23,'Arroz Frito',8.0,'Arroz con verduras, pollo y salsa de soja',7),
 (24,'Paella Valenciana',12.5,'Paella con mariscos y pollo',7),
 (25,'Pasta al Pesto',9.0,'Pasta con salsa pesto y piñones',8),
 (26,'Ensalada César',7.0,'Ensalada con pollo, lechuga, crutones y salsa César',8),
 (27,'Pizza Cuatro Quesos',9.5,'Pizza con mozzarella, cheddar, gouda y azul',9),
 (28,'Lasagna Bolognese',11.0,'Lasagna con carne y salsa bechamel',9),
 (29,'Maki Rolls',13.0,'Rollos de sushi con pepino, aguacate y atún',10),
 (30,'Tempura de Mariscos',14.0,'Tempura de camarones y calamares',10);
INSERT INTO "repartidores" ("id","nif","nombre","id_pedido_asignado","vehiculo") VALUES (6,'12345678A','Juan Gómez',1,'bicicleta'),
 (7,'23456789B','Luis Pérez',2,'moto'),
 (8,'34567890C','Marta Rodríguez',3,'coche'),
 (9,'45678901D','Pedro Sánchez',4,'bicicleta'),
 (10,'56789012E','Isabel Díaz',5,'moto');
INSERT INTO "restaurantes" ("id","nombre","direccion","categoria","telefono","horario","calificacion") VALUES (6,'Restaurante La Toscana','Calle Falsa 123, Madrid','Italiana','912345678','12:00 - 23:00',4.5),
 (7,'Sushi Bar Tokyo','Avenida de la Paz 456, Barcelona','Japonesa','923456789','12:00 - 22:00',4.8),
 (8,'El Camino','Calle Mayor 789, Valencia','Mexicana','934567890','10:00 - 24:00',4.2),
 (9,'Restaurante El Grill','Plaza de la Constitución 321, Sevilla','Rápida','945678901','08:00 - 21:00',3.9),
 (10,'La Cantina','Calle de Gran Vía 654, Zaragoza','Vegetariana','956789012','09:00 - 20:00',4.1),
 (11,'El Rincón Andaluz','Calle del Sol 555, Sevilla','Andaluza','967890123','10:00 - 22:00',4.4),
 (12,'El Asador','Calle de la Luna 111, Madrid','Carnes','978901234','12:00 - 23:00',4.6),
 (13,'El Mexicano','Avenida Cataluña 789, Barcelona','Mexicana','989012345','11:00 - 23:00',3.8),
 (14,'La Pizza Nostra','Calle de Alcalá 100, Madrid','Italiana','990123456','12:00 - 23:00',4.7),
 (15,'Café de la Plaza','Plaza Mayor 222, Madrid','Cafetería','991234567','07:00 - 20:00',4.0);
INSERT INTO "usuarios" ("id","nombre","email","direccion","telefono","fecha_registro") VALUES (6,'Juan Pérez','juan.perez@example.com','Calle Falsa 123, Madrid','612345678','2025-03-09 20:29:23'),
 (7,'Ana Gómez','ana.gomez@example.com','Avenida de la Paz 456, Barcelona','633456789','2025-03-09 20:29:23'),
 (8,'Carlos Martínez','carlos.martinez@example.com','Calle Mayor 789, Valencia','644567890','2025-03-09 20:29:23'),
 (9,'Laura López','laura.lopez@example.com','Plaza de la Constitución 321, Sevilla','655678901','2025-03-09 20:29:23'),
 (12,'Alberto Ruiz','alberto.ruiz@example.com','Calle San Juan 876, Valencia','688901234','2025-03-09 20:29:23'),
 (13,'Lucía Díaz','lucia.diaz@example.com','Avenida Cataluña 567, Barcelona','699012345','2025-03-09 20:29:23'),
 (14,'Miguel González','miguel.gonzalez@example.com','Calle Princesa 987, Madrid','610123456','2025-03-09 20:29:23'),
 (15,'Pablo Torres','pablo.torres@example.com','Calle de Gran Vía 111, Madrid','611234567','2025-03-09 20:29:23'),
 (17,'Pedro Sánchez','pedro.sanchez@example.com','Calle de Gran Vía 654, Zaragoza','666789012','2025-03-09 20:42:03'),
 (18,'Sofía Pérez','sofia.perez@example.com','Calle de Alcalá 345, Madrid','677890123','2025-03-09 20:42:03'),
 (19,'adriag','1@gmail.com',NULL,'dfdfdf','2025-03-09 20:42:51');
COMMIT;
