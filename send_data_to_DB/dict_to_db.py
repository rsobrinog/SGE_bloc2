import psycopg2

def connection_db():
    conn = psycopg2.connect(
            database="the_bear",
            password="admin",
            user="admin",
            host="localhost",
            port="5432"
        )

    return conn

def send_data_to_db(data):
    print(data)
    conn = connection_db()
    cursor = conn.cursor()
    x = 0
    for i in data["Nombre_Cliente"]:
        sql_insert = ('INSERT INTO Clientes ("nombre_cliente", "dirección_cliente", "teléfono_cliente", "correo_electrónico_cliente", "fecha_cumpleaños") VALUES (?,?,?,?,?)')
        values = (data["Nombre_Cliente"][x], data["dirección_cliente"][x], data["teléfono_cliente"][x], data["correo_electrónico_cliente"][x], data["fecha_cumpleaños"][x])

        cursor.execute(sql_insert, values)
        conn.commit()
        
        x += 1

data = {'ID_Cliente': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
        'Nombre_Cliente': ['Roger', 'Juan Manuel', 'Josep Oriol', 'Mireia', 'Alba', 'Miquel', 'Martin', 'Miquel Angel', 'Carlota', 'Andreu', 'David', 'Maria', 'Marta', 'Montse', 'Vivian', 'Xavier', 'Antonio', 'Sara', 'Pep', 'Albert', 'Carla', 'Mariona', 'Laura', 'Leonard', 'Marina', 'Anna', 'Valeria', 'Veronica', 'Estefania', 'Aleix'],
        'dirección_cliente': ['Roger', 'Juan Manuel', 'Josep Oriol', 'Mireia', 'Alba', 'Miquel', 'Martin', 'Miquel Angel', 'Carlota', 'Andreu', 'David', 'Maria', 'Marta', 'Montse', 'Vivian', 'Xavier', 'Antonio', 'Sara', 'Pep', 'Albert', 'Carla', 'Mariona', 'Laura', 'Leonard', 'Marina', 'Anna', 'Valeria', 'Veronica', 'Estefania', 'Aleix']}
send_data_to_db(data)



