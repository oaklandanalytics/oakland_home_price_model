import pandas as pd
import numpy as np
import statsmodels.api as sm
from sample import schools

df = pd.read_csv("sample_with_walkscores.csv")

df["LOT SIZE"] = df["LOT SIZE"].fillna(df["LOT SIZE"].mean())
df["historic"] = (df["YEAR BUILT"] < 1940).astype("int")
df["multifamily"] = ~df["HOA/MONTH"].isnull().astype("int")
df["FAVORITE"] = (df["FAVORITE"] == "Y").astype("int")

df["recent"] = (df.days_ago < 45).astype("int")
df["target"] = (df.days_ago < 45).astype("int") * (df.glenview + df.crocker_highlands)
df["thisspring"] = df.eval("150 > days_ago >= 45").astype("int")
df["lastfall"] = df.eval("250 > days_ago >= 150").astype("int")

y = df["$/SQUARE FEET"]

x = df[[
	"SQUARE FEET",
	"BATHS",
	"recent",
	"target",
	"thisspring",
	"lastfall",
	"FAVORITE",
	"walkscore",
	"LOT SIZE",
	"historic"
] + schools[1:]]

print len(df)

x = sm.add_constant(x)
res = sm.OLS(y, x).fit()

print res.params