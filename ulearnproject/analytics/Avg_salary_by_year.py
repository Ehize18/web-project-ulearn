import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("ALL_Salary_in_Rubble_fixed.csv")
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
df2 = pd.read_csv("Salary_in_Rubble_fixed.csv")
df2["published_at"] = pd.to_datetime(df2["published_at"], utc=True)
df["year"] = df["published_at"].dt.strftime("%Y")
df2["year"] = df2["published_at"].dt.strftime("%Y")

gpy1 = pd.DataFrame(df.groupby("year")["salary_in_rub"].mean())
gpy2 = pd.DataFrame(df2.groupby("year")["salary_in_rub"].mean())

df3 = gpy1.merge(gpy2, how="left", right_index=True, left_index=True)
df3.columns = ["Все вакансии", "Full Stack"]

df3.plot(kind="bar")
plt.savefig("Full_by_year.png")

df.to_csv("Full_by_year.csv")