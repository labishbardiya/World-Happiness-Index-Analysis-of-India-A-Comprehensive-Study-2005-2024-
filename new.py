import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests

# 1) Pull India GDP per capita (current US$) from World Bank API safely
wb_url = "https://api.worldbank.org/v2/country/IND/indicator/NY.GDP.PCAP.CD?format=json&per_page=70"

try:
    response = requests.get(wb_url, timeout=10)
    response.raise_for_status()  # raise if HTTP error
    data = response.json()
    if len(data) > 1 and isinstance(data[1], list):
        gdp_json = data[1]
    else:
        raise ValueError("Unexpected World Bank API structure.")
except Exception as e:
    print(f"Error fetching GDP data: {e}")
    gdp_json = []  # fallback empty list

# Convert to DataFrame only if data is valid
if gdp_json:
    gdp = pd.DataFrame(gdp_json)[["date", "value"]].rename(columns={"date": "Year", "value": "GDP_pc_USD"})
    gdp["Year"] = gdp["Year"].astype(int)
    gdp = gdp[(gdp["Year"] >= 2013) & (gdp["Year"] <= 2024)].sort_values("Year")
else:
    # Manual fallback (if API fails)
    print("Using fallback GDP data.")
    gdp = pd.DataFrame({
        "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
        "GDP_pc_USD": [1458, 1560, 1605, 1740, 1983, 2100, 2160, 1900, 2200, 2380, 2550, 2720]
    })

# 2) India happiness scores (Cantril ladder 0–10) for 2013–2024 (from WHR)
happiness = pd.DataFrame({
    "Year": [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Happiness_Score": [4.77, 4.57, 4.40, 4.32, 4.19, 4.02, 3.57, 3.82, 3.78, 4.04, 4.05, 4.39]
})

# 3) Merge and drop missing
df = pd.merge(gdp, happiness, on="Year", how="inner").dropna()

# 4) Linear regression and visualization
x = df["GDP_pc_USD"].values
y = df["Happiness_Score"].values
coef = np.polyfit(x, y, 1)
poly_fn = np.poly1d(coef)
y_pred = poly_fn(x)
r2 = 1 - (np.sum((y - y_pred) ** 2) / np.sum((y - y.mean()) ** 2))

plt.figure(figsize=(7.5, 5.0))
plt.scatter(x, y, color="#1f77b4", label="India, 2013–2024")
plt.plot(x, y_pred, color="#ff7f0e", label=f"Linear fit (R²={r2:.2f})")
plt.title("India: GDP per Capita vs Happiness Score (2013–2024)")
plt.xlabel("GDP per capita (current US$)")
plt.ylabel("Happiness score (0–10)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
