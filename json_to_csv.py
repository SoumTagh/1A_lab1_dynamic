import json
import pandas as pd

# read the JSON file
with open("producthunt_first_page.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# convert to DataFrame
df = pd.DataFrame(products)
print(df)

# save to CSV
df.to_csv("producthunt_first_page.csv", index=False, encoding="utf-8")
print("CSV saved!")