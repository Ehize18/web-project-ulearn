import pandas as pd
import re

searchfor = [re.escape(i) for i in ['fullstack', 'фулстак', 'фуллтак', 'фуллстэк', 'фулстэк', 'full stack']]

df = pd.read_csv("vacancies.csv")
df = df[df["name"].str.contains(r'|'.join(searchfor), flags=re.IGNORECASE)]

df.to_csv("fullstack.csv")