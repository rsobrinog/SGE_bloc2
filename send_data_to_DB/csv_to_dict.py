import pandas as pd
import dict_to_db


def csv_to_dict(table):
    df = pd.read_csv(table)
    data = df.to_dict(orient='list')

    return data


def send_data():
    data = csv_to_dict("Clientes.csv")
    dict_to_db.send_data_to_db(data)
    #print(csv_to_dict("Clientes2.csv"))
    #print(type(csv_to_dict("Clientes2.csv")))
    return {"Data sended succesfully"}


send_data()
# print(csv_to_dict("Cuentas.csv"))
# print(csv_to_dict("menu.csv"))
# print(csv_to_dict("Mesas.csv"))
# print(csv_to_dict("Métodos_de_Pago.csv"))
# print(csv_to_dict("Pedidos.csv"))
# print(csv_to_dict("Ventas.csv"))
# print(csv_to_dict("restaurantes.csv"))