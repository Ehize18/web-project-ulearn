import pandas as pd

geo_all_count = pd.read_csv("static/main/data/geo_all_count.csv", index_col=0)
geo_all_count.columns = ["count"]
geo_all_count = geo_all_count.sort_values("count", ascending=False)
geo_all_count = geo_all_count.to_dict(orient="index")


geo_fullstack_count = pd.read_csv("static/main/data/geo_fullstack_count.csv", index_col=0)
geo_fullstack_count.columns = ["count"]
geo_fullstack_count = geo_fullstack_count.sort_values("count", ascending=False)
geo_fullstack_count = geo_fullstack_count.to_dict(orient="index")

geo_all_salary = pd.read_csv("static/main/data/geo_all_salary.csv", index_col=0)
geo_all_salary.columns = ["salary"]
geo_all_salary = geo_all_salary.sort_values("salary", ascending=False)
geo_all_salary = geo_all_salary.to_dict(orient="index")

geo_fullstack_salary = pd.read_csv("static/main/data/geo_fullstack_salary.csv", index_col=0)
geo_fullstack_salary.columns = ["salary"]
geo_fullstack_salary = geo_fullstack_salary.sort_values("salary", ascending=False)
geo_fullstack_salary = geo_fullstack_salary.to_dict(orient="index")