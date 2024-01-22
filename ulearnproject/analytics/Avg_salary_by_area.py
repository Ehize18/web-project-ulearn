import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

all = pd.read_csv("ALL_Salary_in_Rubble_fixed.csv", index_col=0)
fullstack = pd.read_csv("Salary_in_Rubble_fixed.csv", index_col=0)

gpy1 = all.groupby("area_name")["salary_in_rub"].mean().sort_values(ascending=True)
gpy2 = fullstack.groupby("area_name")["salary_in_rub"].mean().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(10, 655.35))
gpy1.plot(kind="barh", ax=ax)
ax.set_title("Уровень зарплат по городам для всех вакансий")
ax.xaxis.tick_top()
plt.tight_layout()
plt.savefig("geo_all_salary.png")

plt.clf()
plt.close()

fig, ax = plt.subplots(figsize=(10, 100))
gpy2.plot(kind="barh", ax=ax)
ax.set_title("Уровень зарплат по городам для вакансий Fullstack разработчика")
ax.xaxis.tick_top()
plt.tight_layout()
plt.savefig("geo_fullstack_salary.png")

tmp1 = pd.DataFrame(gpy1)
tmp2 = pd.DataFrame(gpy2)

tmp1.to_csv("geo_all_salary.csv")
tmp2.to_csv("geo_fullstack_salary.csv")