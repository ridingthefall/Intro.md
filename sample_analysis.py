# Sample data analysis for growth metrics

import pandas as pd

# Example engagement data
data = {
    "Campaign": ["Email", "Push", "Social"],
    "Impressions": [1200, 800, 1500],
    "Conversions": [60, 50, 120]
}

df = pd.DataFrame(data)

# Calculate conversion rates
df["Conversion_Rate"] = df["Conversions"] / df["Impressions"] * 100

print(df)
