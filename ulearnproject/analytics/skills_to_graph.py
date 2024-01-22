import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("all_skills.csv", index_col=0)

years = df["year"].sort_values().unique()

fig, axes = plt.subplots(nrows=len(years), ncols=1, figsize=(10, 100))

for i, year in enumerate(years):

    ax = axes[i]

    df_year = df[df["year"] == year]
    df_year = df_year.sort_values("count")

    df_year.plot(x="key_skills", y="count", kind="barh", ax=ax)
    ax.set_ylabel("Навык")
    ax.set_xlabel("Количество упоминаний")
    ax.set_title(f"Топ 20 навыков в {year} году")
    ax.get_legend().remove()

plt.tight_layout()
plt.savefig("all_skils.png")