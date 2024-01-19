import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vacancies.csv")
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
df2 = pd.read_csv("fullstack.csv")
df2["published_at"] = pd.to_datetime(df2["published_at"], utc=True)

df["year"] = df["published_at"].dt.strftime("%Y")
df2["year"] = df2["published_at"].dt.strftime("%Y")

gpy1 = df.groupby("year").size()
gpy2 = df2.groupby("year").size()

gpy1.plot(kind="bar")
plt.savefig("All_count_by_year.png")
plt.close()

gpy2.plot(kind="bar")
plt.savefig("Prof_count_by_year.png")