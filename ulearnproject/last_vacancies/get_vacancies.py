import requests as req
import pandas as pd
import openpyxl
import json
import re

url = "https://api.hh.ru/vacancies"

params = {"text": "fullstack OR фулстак OR фуллтак OR фуллстэк OR фулстэк OR full stack",
          "search_field": "name",
          "per_page": "10",
          "order_by": "publication_time",
          "period": "1"}
response = req.get(url, params=params)

dct = json.loads(response.text)

df = pd.DataFrame(dct["items"])
vacancies_list = []
for id in df["id"]:
    response = req.get(f"{url}/{id}")
    vacancies_list.append(json.loads(response.text))
df = pd.DataFrame(vacancies_list)

df = df[["id", "name", "description", "key_skills", "employer", "salary", "area", "published_at"]]
df.set_index("id", inplace=True)

df["key_skills"] = df["key_skills"].apply(lambda x: ", ".join([d["name"] for d in x]))
df["employer"] = df["employer"].apply(lambda x: x["name"])
df["area"] = df["area"].apply(lambda x: x["name"])
df["salary"] = df["salary"].apply(
    lambda x: "Не указано" if x is None else
    (f"От {x['from']} " if x['from'] is not None else "") +
    (f"до {x['to']} " if x['to'] is not None else "") +
    (f"{x['currency']} ") +
    (f"Без вычета налогов" if x['gross'] else "С вычетом"))
df["description"] = df["description"].apply(lambda x: re.sub(r"<[^>]+>", '', x))
df["published_at"] = df["published_at"].apply(lambda x: re.sub(r"T.+", '', x))
vacancies = df.to_dict(orient="index")
