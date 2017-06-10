import pandas as pd
import numpy as np

schools = ["glenview", "chabot", "peralta", "crocker_highlands", "piedmont", "emerson"]

dfs = []
for school in schools:
    df = pd.read_csv("data/%s.csv" % school)
    df[school] = 1
    dfs.append(df)

df = pd.concat(dfs)

for school in schools:
	df[school] = df[school].fillna(0)

df = df[~df["SQUARE FEET"].isnull()]
df = df[df["PROPERTY TYPE"] == "Single Family Residential"]
df = df[df.STATUS == "Sold"]
df = df.query("PRICE < 1500000 and PRICE > 600000")

df["days_ago"] = 17327 - \
	pd.to_timedelta(pd.to_datetime(df["SOLD DATE"], infer_datetime_format=True)).dt.days

df = df[df.days_ago < 450]

df.to_csv("sample.csv", index=False)