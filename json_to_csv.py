import json
import pandas as pd

# reading the JSON file
with open("producthunt_first_page.json", "r", encoding="utf-8") as f:
    products = json.load(f)

# converting to dataframe
df = pd.DataFrame(products)
print(df)

# saving to CSV
df.to_csv("producthunt_first_page.csv", index=False, encoding="utf-8")
print("CSV saved!")
