import pandas as pd


def csv_to_dict():
    df = pd.read_csv("")
    data = df.to_dict(oritent='list')

    return data

print(csv_to_dict())
