import pandas as pd


def get_stock_list():

    df = pd.read_csv("stock_list.csv", dtype=str)

    return df.sort_values("code").reset_index(drop=True)