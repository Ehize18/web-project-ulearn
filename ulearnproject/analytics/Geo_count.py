import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("vacancies.csv")
df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
df2 = pd.read_csv("fullstack.csv")
df2["published_at"] = pd.to_datetime(df2["published_at"], utc=True)
df.reset_index(inplace=True)

df["year"] = df["published_at"].dt.strftime('%Y')
df2["year"] = df2["published_at"].dt.strftime('%Y')

gpy1 = (df.groupby("area_name").size() / len(df) * 100).sort_values(ascending=True)
gpy2 = (df2.groupby("area_name").size() / len(df2) * 100).sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 655.35))
gpy1.plot(kind="barh", ax=ax)
ax.set_title("Доля всех вакансий по городам")
ax.xaxis.tick_top()
plt.tight_layout()
plt.savefig("geo_all_count.png")

plt.clf()
plt.close()

fig, ax = plt.subplots(figsize=(10, 100))
gpy2.plot(kind="barh", ax=ax)
ax.set_title("Доля вакансий Fullstack разработчика по городам")
ax.xaxis.tick_top()
plt.tight_layout()
plt.savefig("geo_fullstack_count.png")

tmp1 = pd.DataFrame(gpy1)
tmp2 = pd.DataFrame(gpy2)
tmp1.to_csv("geo_all_count.csv")
tmp2.to_csv("geo_fullstack_count.csv")
