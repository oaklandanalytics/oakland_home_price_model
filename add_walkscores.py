import pandas as pd
import requests

apiKey = "f4a576e5298b25b26885df3c6264b30a"

df = pd.read_csv("sample.csv")

rows = []

for index, row in df.iterrows():
	try:
		address, lat, lon = row.ADDRESS + ", Oakland, CA", row.LATITUDE, row.LONGITUDE
		print address, lat, lon
		url = "http://api.walkscore.com/score?format=json&address={}&lat={}&lon={}&wsapikey={}".format(address, lat, lon, apiKey)
		r = requests.get(url)
		walkscore = r.json()["walkscore"]
		row["walkscore"] = walkscore
		rows.append(row)
	except:
		pass

pd.DataFrame.from_records(rows).to_csv("sample_with_walkscores.csv", index=False)