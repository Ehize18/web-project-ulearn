import pandas as pd

df = pd.read_csv("fullstack.csv")
df["year"] = pd.to_datetime(df["published_at"], utc=True).dt.strftime("%Y")

df["key_skills"] = df["key_skills"].str.split("\n")
df = df[["key_skills", "year"]]

df = df.explode("key_skills")
df = df.groupby(["year", "key_skills"]).size()
df = df.sort_values(ascending=False)
df = df.groupby(level=0).head(20)

df = df.reset_index(name='count')
df.to_csv('fullstack_skills.csv')