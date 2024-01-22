import pandas as pd

all_skills = pd.read_csv("static/main/data/all_skills.csv", index_col=0)
all_skills = all_skills.sort_values(["year", "count"], ascending=[True, False])
all_skills.columns = ["year", "skill", "count"]
all_skills = all_skills.to_dict(orient="index")

fullstack_skills = pd.read_csv("static/main/data/fullstack_skills.csv", index_col=0)
fullstack_skills = fullstack_skills.sort_values(["year", "count"], ascending=[True, False])
fullstack_skills.columns = ["year", "skill", "count"]
fullstack_skills = fullstack_skills.to_dict(orient="index")