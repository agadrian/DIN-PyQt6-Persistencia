import sqlite3 as db

def create_tables():
    conn = db.connect("database.db")
    cursor = conn.cursor()

    sql_statements = [
        """DROP TABLE IF EXISTS usuarios;""",
        """DROP TABLE IF EXISTS restaurantes;""",
        """DROP TABLE IF EXISTS platos;""",
        """DROP TABLE IF EXISTS pedidos;""",
        """DROP TABLE IF EXISTS detalles_pedido;""",
        """DROP TABLE IF EXISTS repartidores;""",

        """PRAGMA foreign_keys = ON;""",



        """CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            email TEXT UNIQUE NOT NULL, 
            direccion TEXT, 
            telefono TEXT UNIQUE NULL,
            fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );""",
        
        """CREATE TABLE IF NOT EXISTS restaurantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            direccion TEXT NOT NULL, 
            categoria TEXT, 
            telefono TEXT UNIQUE,
            horario TEXT,
            calificacion REAL CHECK (calificacion >= 0 AND calificacion <= 5)
        );""",
        
        """CREATE TABLE IF NOT EXISTS platos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nombre TEXT NOT NULL, 
            precio REAL NOT NULL CHECK (precio > 0), 
            descripcion TEXT NOT NULL,
            id_restaurante INTEGER NOT NULL, 
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_cliente TEXT NOT NULL, 
            id_restaurante INTEGER NOT NULL, 
            estado TEXT CHECK (estado IN ('pendiente', 'en preparación', 'en camino', 'entregado')), 
            FOREIGN KEY (id_cliente) REFERENCES usuarios(id) ON DELETE CASCADE,
            FOREIGN KEY (id_restaurante) REFERENCES restaurantes(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS detalles_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            id_pedido INTEGER NOT NULL, 
            id_plato INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK (cantidad > 0), 
            FOREIGN KEY (id_pedido) REFERENCES pedidos(id) ON DELETE CASCADE, 
            FOREIGN KEY (id_plato) REFERENCES platos(id) ON DELETE CASCADE
        );""",
        
        """CREATE TABLE IF NOT EXISTS repartidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nif TEXT UNIQUE NOT NULL, 
            nombre TEXT NOT NULL, 
            id_pedido_asignado INTEGER, 
            vehiculo TEXT, 
            FOREIGN KEY (id_pedido_asignado) REFERENCES pedidos(id) ON DELETE SET NULL
        );""",
    ]


    for i in sql_statements:
        cursor.execute(i)
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = cursor.fetchall()


    print("\nTablas en la BD:")
    for tabla in tablas:
        print(tabla[0])


    conn.commit()
    conn.close()




def insertar_datos_grandes():
    conn = db.connect("database.db")
    cursor = conn.cursor()

    # Desactivar restricciones de claves foráneas temporalmente
    cursor.execute("PRAGMA foreign_keys = OFF;")
    
    # Insertar datos en la tabla 'usuarios' (10 usuarios)
    cursor.executemany("""
    INSERT INTO usuarios (nombre, email, direccion, telefono) VALUES (?, ?, ?, ?);
    """, [
        ('Juan Pérez', 'juan.perez@example.com', 'Calle Falsa 123, Madrid', '612345678'),
        ('Ana Gómez', 'ana.gomez@example.com', 'Avenida de la Paz 456, Barcelona', '633456789'),
        ('Carlos Martínez', 'carlos.martinez@example.com', 'Calle Mayor 789, Valencia', '644567890'),
        ('Laura López', 'laura.lopez@example.com', 'Plaza de la Constitución 321, Sevilla', '655678901'),
        ('Pedro Sánchez', 'pedro.sanchez@example.com', 'Calle de Gran Vía 654, Zaragoza', '666789012'),
        ('Sofía Pérez', 'sofia.perez@example.com', 'Calle de Alcalá 345, Madrid', '677890123'),
        ('Alberto Ruiz', 'alberto.ruiz@example.com', 'Calle San Juan 876, Valencia', '688901234'),
        ('Lucía Díaz', 'lucia.diaz@example.com', 'Avenida Cataluña 567, Barcelona', '699012345'),
        ('Miguel González', 'miguel.gonzalez@example.com', 'Calle Princesa 987, Madrid', '610123456'),
        ('Pablo Torres', 'pablo.torres@example.com', 'Calle de Gran Vía 111, Madrid', '611234567'),
    ])

    # Insertar datos en la tabla 'restaurantes' (10 restaurantes)
    cursor.executemany("""
    INSERT INTO restaurantes (nombre, direccion, categoria, telefono, horario, calificacion) VALUES (?, ?, ?, ?, ?, ?);
    """, [
        ('Restaurante La Toscana', 'Calle Falsa 123, Madrid', 'Italiana', '912345678', '12:00 - 23:00', 4.5),
        ('Sushi Bar Tokyo', 'Avenida de la Paz 456, Barcelona', 'Japonesa', '923456789', '12:00 - 22:00', 4.8),
        ('El Camino', 'Calle Mayor 789, Valencia', 'Mexicana', '934567890', '10:00 - 24:00', 4.2),
        ('Restaurante El Grill', 'Plaza de la Constitución 321, Sevilla', 'Rápida', '945678901', '08:00 - 21:00', 3.9),
        ('La Cantina', 'Calle de Gran Vía 654, Zaragoza', 'Vegetariana', '956789012', '09:00 - 20:00', 4.1),
        ('El Rincón Andaluz', 'Calle del Sol 555, Sevilla', 'Andaluza', '967890123', '10:00 - 22:00', 4.4),
        ('El Asador', 'Calle de la Luna 111, Madrid', 'Carnes', '978901234', '12:00 - 23:00', 4.6),
        ('El Mexicano', 'Avenida Cataluña 789, Barcelona', 'Mexicana', '989012345', '11:00 - 23:00', 3.8),
        ('La Pizza Nostra', 'Calle de Alcalá 100, Madrid', 'Italiana', '990123456', '12:00 - 23:00', 4.7),
        ('Café de la Plaza', 'Plaza Mayor 222, Madrid', 'Cafetería', '991234567', '07:00 - 20:00', 4.0),
    ])

    # Insertar datos en la tabla 'platos' (20 platos, asignando id_restaurante válidos)
    cursor.executemany("""
    INSERT INTO platos (nombre, precio, descripcion, id_restaurante) VALUES (?, ?, ?, ?);
    """, [
        ('Pizza Margherita', 8.50, 'Pizza clásica con tomate, mozzarella y albahaca', 1),
        ('Spaghetti Carbonara', 10.00, 'Spaghetti con salsa cremosa de huevo y panceta', 1),
        ('Sushi Rolls', 12.00, 'Rollos de sushi con atún, salmón y aguacate', 2),
        ('Sashimi de Salmón', 15.00, 'Salmón fresco en láminas finas', 2),
        ('Tacos al Pastor', 6.50, 'Tacos de cerdo marinados con piña y cilantro', 3),
        ('Burritos de Carne', 7.00, 'Burritos con carne, arroz, frijoles y salsa picante', 3),
        ('Hamburguesa El Grill', 9.00, 'Hamburguesa de carne con queso cheddar, cebolla caramelizada', 4),
        ('Hot Dog con Mostaza', 4.50, 'Perro caliente con mostaza, ketchup y cebolla', 4),
        ('Ensalada Vegana', 6.00, 'Ensalada con quinoa, aguacate, zanahoria y tomate', 5),
        ('Hamburguesa Vegana', 7.50, 'Hamburguesa con pan de avena y proteína vegetal', 5),
        ('Bocadillo de Jamón', 5.50, 'Bocadillo con jamón serrano y tomate', 6),
        ('Croquetas Caseras', 4.00, 'Croquetas de pollo y jamón', 6),
        ('Arroz Frito', 8.00, 'Arroz con verduras, pollo y salsa de soja', 7),
        ('Paella Valenciana', 12.50, 'Paella con mariscos y pollo', 7),
        ('Pasta al Pesto', 9.00, 'Pasta con salsa pesto y piñones', 8),
        ('Ensalada César', 7.00, 'Ensalada con pollo, lechuga, crutones y salsa César', 8),
        ('Pizza Cuatro Quesos', 9.50, 'Pizza con mozzarella, cheddar, gouda y azul', 9),
        ('Lasagna Bolognese', 11.00, 'Lasagna con carne y salsa bechamel', 9),
        ('Maki Rolls', 13.00, 'Rollos de sushi con pepino, aguacate y atún', 10),
        ('Tempura de Mariscos', 14.00, 'Tempura de camarones y calamares', 10),
    ])

    # Insertar datos en la tabla 'pedidos' (20 pedidos, asignando id_cliente e id_restaurante válidos)
    cursor.executemany("""
    INSERT INTO pedidos (id_cliente, id_restaurante, estado) VALUES (?, ?, ?);
    """, [
        (1, 1, 'pendiente'),
        (2, 2, 'en preparación'),
        (3, 3, 'en camino'),
        (4, 4, 'entregado'),
        (5, 5, 'pendiente'),
        (6, 6, 'en preparación'),
        (7, 7, 'en camino'),
        (8, 8, 'entregado'),
        (9, 9, 'pendiente'),
        (10, 10, 'en preparación'),
    ])

    # Insertar datos en la tabla 'detalles_pedido' (50 detalles de pedido, asignando id_pedido e id_plato válidos)
    cursor.executemany("""
    INSERT INTO detalles_pedido (id_pedido, id_plato, cantidad) VALUES (?, ?, ?);
    """, [
        (1, 1, 2),
        (2, 2, 1),
        (3, 3, 3),
        (4, 4, 1),
        (5, 5, 2),
        (6, 6, 2),
        (7, 7, 3),
        (8, 8, 1),
        (9, 9, 2),
        (10, 10, 3),
    ])

    # Insertar datos en la tabla 'repartidores' (5 repartidores, asignando id_pedido_asignado válidos)
    cursor.executemany("""
    INSERT INTO repartidores (nif, nombre, id_pedido_asignado, vehiculo) VALUES (?, ?, ?, ?);
    """, [
        ('12345678A', 'Juan Gómez', 1, 'bicicleta'),
        ('23456789B', 'Luis Pérez', 2, 'moto'),
        ('34567890C', 'Marta Rodríguez', 3, 'coche'),
        ('45678901D', 'Pedro Sánchez', 4, 'bicicleta'),
        ('56789012E', 'Isabel Díaz', 5, 'moto'),
    ])

    # Volver a activar las restricciones de claves foráneas
    cursor.execute("PRAGMA foreign_keys = ON;")

    conn.commit()
    conn.close()
    print("Datos grandes insertados correctamente.")







def ver_usuarios():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()

    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("No hay usuarios en la base de datos.")

    

def exportSQL():
    conn = db.connect("database.db")
    cursor = conn.cursor()
    
    # Abrir el archivo .sql para guardar el volcado
    with open("exportado.sql", "w") as sql_file:
        # Volcar toda la base de datos usando iterdump
        for line in conn.iterdump():
            sql_file.write(f"{line}\n")
    
    print("Exportación completada en el archivo exportado.sql")
    
    conn.close()
    


def vaciar_tablas():
    conn = db.connect("database.db")
    cursor = conn.cursor()

    # Lista de las tablas en la base de datos
    tablas = ['usuarios', 'restaurantes', 'platos', 'pedidos', 'detalles_pedido', 'repartidores']

    # Vaciar cada tabla
    for tabla in tablas:
        cursor.execute(f"DELETE FROM {tabla};")
        print(f"Datos eliminados de la tabla {tabla}.")

    # Confirmar los cambios
    conn.commit()
    conn.close()
    print("Todas las tablas han sido vaciadas.")

if __name__ == "__main__":
    #create_tables()
    #ver_usuarios()
    exportSQL()
    #insertar_datos_grandes()
    #vaciar_tablas()