import psycopg2

def create_tables():
    conn = psycopg2.connect(
        database="the_bear",
        password="admin",
        user="admin",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    sql_restaurant = '''
        CREATE TABLE Restaurantes (
        ID_Restaurante INT PRIMARY KEY,
        Nombre VARCHAR(100),
        Dirección VARCHAR(200),
        Teléfono VARCHAR(20),
        Correo_Electrónico VARCHAR(100));'''

    sql_menu = '''
        CREATE TABLE menu (
        ID_Plato INT PRIMARY KEY,
        Nombre_Plato VARCHAR(100),
        Descripción_Plato TEXT,
        Nivel_Dificultad VARCHAR(20),
        Precio DECIMAL(10, 2),
        opcion_menu VARCHAR(20) CHECK (opcion_menu IN ('vegetariano', 'vegano', 'omnivoro'));'''

    sql_clients = '''
        CREATE TABLE Clientes (
        ID_Cliente INT PRIMARY KEY,
        Nombre_Cliente VARCHAR(100),
        Dirección_Cliente VARCHAR(200),
        Teléfono_Cliente VARCHAR(20),
        Correo_Electrónico_Cliente VARCHAR(100),
        Fecha_Cumpleaños DATE);'''

    sql_orders = '''CREATE TABLE Pedidos (
        ID_Pedido INT PRIMARY KEY,
        ID_Cliente INT,
        Fecha_Pedido DATE,
        Tipo_Entrega VARCHAR(20),
        Estado_Pedido VARCHAR(20),
        FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente));'''

    sql_tables = '''CREATE TABLE Mesas (
        ID_Mesa INT PRIMARY KEY,
        Capacidad_Mesa INT,
        Estado_Mesa VARCHAR(20));'''

    sql_booking = '''CREATE TABLE Reservas (
        ID_Reserva INT PRIMARY KEY,
        ID_Cliente INT,
        ID_Mesa INT,
        Fecha_Reserva DATE,
        Hora_Reserva TIME,
        FOREIGN KEY (ID_Cliente) REFERENCES Clientes(ID_Cliente),
        FOREIGN KEY (ID_Mesa) REFERENCES Mesas(ID_Mesa));'''

    sql_sales = '''CREATE TABLE Ventas (
        ID_Venta INT PRIMARY KEY,
        ID_Pedido INT,
        Fecha_Venta DATE,
        Subtotal DECIMAL(10, 2),
        Total DECIMAL(10, 2),
        Pago_Tarjeta BOOLEAN,
        FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido));'''

    sql_method_payment = '''CREATE TABLE Métodos_de_Pago (
        ID_Método_Pago INT PRIMARY KEY,
        Nombre_Método_Pago VARCHAR(100));'''

    sql_account = '''CREATE TABLE Cuentas (
        ID_Cuenta INT PRIMARY KEY,
        ID_Pedido INT,
        ID_Método_Pago INT,
        Fecha_Emisión_Cuenta DATE,
        Total_Cuenta DECIMAL(10, 2),
        FOREIGN KEY (ID_Pedido) REFERENCES Pedidos(ID_Pedido),
        FOREIGN KEY (ID_Método_Pago) REFERENCES Métodos_de_Pago(ID_Método_Pago));'''

    queries = [sql_restaurant, sql_menu, sql_clients, sql_orders, sql_tables, sql_booking, sql_sales, sql_method_payment, sql_account]

    for query in queries:
        cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close()

    return {"Tables created succesfully"}

create_tables()