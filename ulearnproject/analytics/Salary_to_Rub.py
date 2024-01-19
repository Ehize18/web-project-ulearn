import numpy as np
import pandas as pd
import requests

df = pd.read_csv("vacancies.csv")
df['salary'] = df[['salary_from', 'salary_to']].mean(axis=1)
salary_df = df.dropna(subset=["salary"])

salary_df["published_at"] = pd.to_datetime(salary_df["published_at"], utc=True)

valutes = {}
dates = pd.date_range('2000-01-01', '2024-01-01', freq="MS").tolist()
for date in dates:
    print(date)
    date_str = date.strftime("%m/%Y")
    url = f"http://www.cbr.ru/scripts/XML_daily.asp?date_req=01/{date_str}"
    response = requests.get(url)
    valutes[date_str] = response
ruble_salary = []
cnt = salary_df["name"].count()
for id in salary_df.index:
    print(f"{cnt}|{id}")
    temp = salary_df.loc[id, ["salary", "salary_currency", "published_at"]]
    temp["salary_currency"] = temp["salary_currency"].replace("BYR", "BYN")
    if temp["salary_currency"] == "RUR":
        ruble_salary.append(float(temp["salary"]))
    else:
        date_str = temp["published_at"].strftime("%m/%Y")
        response = valutes[date_str]
        if response.status_code == 200:
            dff = pd.read_xml(response.text, encoding='cp1251')
            dff["CharCode"] = dff["CharCode"].replace("BYR", "BYN")
            try:
                rate = dff.loc[dff["CharCode"] == temp["salary_currency"], "VunitRate"].item()
                ruble_salary.append(float(temp["salary"]) * float(rate.replace(',', '.')))
            except:
                ruble_salary.append(np.nan)

salary_df["salary_in_rub"] = ruble_salary
salary_df.to_csv("ALL_Salary_in_Rubble.csv")
