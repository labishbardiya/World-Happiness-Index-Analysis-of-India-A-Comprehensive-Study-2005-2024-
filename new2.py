import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# ========= CONFIG =========
OUT_DIR = os.path.join(os.getcwd(), "plots")
INDIA = "India"
START_YEAR = 2011
END_YEAR = 2024

# ========= 1) STATIC DATA (HAPPINESS + SOCIAL SUPPORT) =========
# India’s Cantril ladder (life evaluation) scores (WHR/OWID) — 2011–2024
happiness_data = {
    "Year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Happiness_Score": [5.159, 5.094, 4.770, 4.565, 4.402, 4.315, 4.189, 4.015, 3.573, 3.819, 3.787, 4.039, 4.050, 4.392],
}

# Example global “Social support” distribution (share with someone to count on, 0–1)
# Replace later with WHR table for your edition if desired.
social_support_data = {
    "Country": [
        "Finland", "Denmark", "Iceland", "Israel", "Netherlands", "Sweden",
        "Norway", "Switzerland", "Australia", "New Zealand", "India", "Afghanistan"
    ],
    "Social_support": [0.96, 0.95, 0.94, 0.93, 0.92, 0.91, 0.91, 0.90, 0.89, 0.88, 0.67, 0.37],
}
latest_social_support_year = 2024

# ========= 2) FETCH GDP (World Bank API with fallback) =========
def get_wb_gdp_per_capita(code="IND", start=START_YEAR, end=END_YEAR):
    url = f"https://api.worldbank.org/v2/country/{code}/indicator/NY.GDP.PCAP.CD?format=json&per_page=20000"
    try:
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        data = r.json()
        rows = data[1]
        records = []
        for row in rows:
            if row.get("value") is None:
                continue
            y = int(row.get("date"))
            if start <= y <= end:
                records.append({"Year": y, "GDP_pc_USD": float(row.get("value"))})
        df = pd.DataFrame(records).sort_values("Year").reset_index(drop=True)
        if df.empty:
            raise ValueError("Empty GDP dataframe from API.")
        return df
    except Exception as e:
        print(f"⚠️ World Bank API unavailable ({e}). Using fallback GDP data.")
        return pd.DataFrame({
            "Year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
            "GDP_pc_USD": [1464, 1450, 1458, 1572, 1605, 1740, 1983, 2100, 2160, 1900, 2200, 2380, 2550, 2720]
        })

# ========= 3) PLOTTING =========
def plot_gdp_vs_happiness(df_merge, out_path):
    x = df_merge["GDP_pc_USD"].values
    y = df_merge["Happiness_Score"].values

    # Linear fit and R^2
    coef = np.polyfit(x, y, 1)
    poly = np.poly1d(coef)
    y_pred = poly(x)
    r2 = 1 - np.sum((y - y_pred) ** 2) / np.sum((y - y.mean()) ** 2)

    plt.figure(figsize=(7.8, 5.2))
    plt.scatter(x, y, color="#1f77b4", s=60, label=f"{INDIA} ({int(df_merge['Year'].min())}–{int(df_merge['Year'].max())})")
    plt.plot(x, y_pred, color="#ff7f0e", linewidth=2, label=f"Linear fit (R²={r2:.2f})")

    # Year labels
    for _, row in df_merge.iterrows():
        plt.annotate(str(int(row["Year"])), (row["GDP_pc_USD"], row["Happiness_Score"]),
                     textcoords="offset points", xytext=(4, -6), fontsize=8, color="#444")

    plt.title("India: GDP per Capita vs Happiness Score (2011–2024)")
    plt.xlabel("GDP per capita (current US$) — World Bank")
    plt.ylabel("Happiness score (0–10) — Cantril ladder")
    plt.grid(alpha=0.3, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()
    print(f"✅ Saved: {out_path}")

def plot_social_support_distribution(df_ss, year, out_path):
    if INDIA not in df_ss["Country"].values:
        raise ValueError("India not found in provided social support data.")
    india_val = float(df_ss.loc[df_ss["Country"] == INDIA, "Social_support"].iloc[0])

    plt.figure(figsize=(7.8, 5.0))
    plt.hist(df_ss["Social_support"].dropna(), bins=10,
             color="#aec7e8", edgecolor="#1f77b4", alpha=0.85)
    plt.axvline(india_val, color="#d62728", linestyle="--", linewidth=2, label=f"India = {india_val:.2f}")
    plt.title(f"Global Distribution of Social Support ({year})")
    plt.xlabel("Social support (share with someone to count on, 0–1)")
    plt.ylabel("Number of countries")
    plt.grid(alpha=0.25, linestyle=":")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=180)
    plt.close()
    print(f"✅ Saved: {out_path}")

# ========= 4) MAIN =========
def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    print("Output directory:", OUT_DIR)

    # Fetch GDP (WB) and load happiness
    print("\nFetching India GDP per capita (World Bank or fallback)...")
    df_gdp = get_wb_gdp_per_capita()
    df_hap = pd.DataFrame(happiness_data)

    # Merge, print head/tail for verification, and plot scatter
    df_merge = pd.merge(df_gdp, df_hap, on="Year", how="inner").dropna()
    print("\nMerged GDP & Happiness (last rows):")
    print(df_merge.tail(5).to_string(index=False))

    out1 = os.path.join(OUT_DIR, "gdp_vs_happiness_IND_2011_2024.png")
    plot_gdp_vs_happiness(df_merge, out1)

    # Social support figure (using your provided example distribution)
    df_ss = pd.DataFrame(social_support_data)
    out2 = os.path.join(OUT_DIR, f"social_support_distribution_{latest_social_support_year}.png")
    plot_social_support_distribution(df_ss, latest_social_support_year, out2)

    print("\n🎯 All done. Plots saved in:", OUT_DIR)

if __name__ == "__main__":
    main()
