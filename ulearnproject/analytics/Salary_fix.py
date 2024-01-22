import pandas as pd
import openpyxl
import requests

df = pd.read_csv("Salary_in_Rubble.csv", index_col=0)
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)

dates = pd.date_range('2023-01-01', '2024-01-01', freq="MS").tolist()
valutes = {}
for date in dates:
    #print(date)
    date_str = date.strftime("%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{date_str}"
    response = requests.get(url)
    valutes[date_str] = response


def func(dataframe):
    date_str = dataframe["published_at"].strftime("%m/%Y")
    if date_str in valutes.keys():
        response = valutes[date_str]
        df = pd.read_xml(response.text, encoding='cp1251')
        rate = df.loc[df["CharCode"] == dataframe["salary_currency"], "VunitRate"].item()
        dataframe["salary_in_rub"] = float(dataframe["salary"]) * float(rate.replace(',', '.'))
    else:
        response = valutes["02/2023"]
        df = pd.read_xml(response.text, encoding='cp1251')
        rate = df.loc[df["CharCode"] == dataframe["salary_currency"], "VunitRate"].item()
        dataframe["salary_in_rub"] = float(dataframe["salary"]) * float(rate.replace(',', '.'))
    return dataframe


gel_index = df[df["salary_currency"] == "GEL"].index
df.loc[gel_index] = df.loc[gel_index].apply(func, axis=1)

mil_index = df[df["salary_in_rub"] > 10000000].index
df.drop(index=mil_index, inplace=True)
mil_index = df[df["salary_in_rub"] > 10000000].index
df.to_csv("Salary_in_Rubble_fixed.csv")