import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("vacancies.csv")
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
df2 = pd.read_csv("fullstack")
df2["published_at"] = pd.to_datetime(df2["published_at"], utc=True)
df.reset_index(inplace=True)

df["year"] = df["published_at"].dt.strftime('%Y')
df2["year"] = df2["published_at"].dt.strftime('%Y')

gpy1 = df.groupby("area_name")["index"].count() / len(df)
gpy2 = df2.groupby("area_name")["Unnamed: 0"].count() / len(df2)

gpy1.plot(kind="barh", figsize=(15, 655.35))
plt.savefig("geo_all_count.png")
plt.clf()
plt.close()
gpy2.plot(kind="barh", figsize=(15, 100))
plt.savefig("geo_prof_count.png")

tmp1 = pd.DataFrame(gpy1)
tmp2 = pd.DataFrame(gpy2)
df3 = tmp1.merge(tmp2, how="left", left_index=True, right_index=True)
df3.columns = ["Все", "Профессия"]

df3.to_csv("geo_all_count.csv")
