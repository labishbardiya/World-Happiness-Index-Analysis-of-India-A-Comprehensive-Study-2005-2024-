
# Create comprehensive dataset with additional variables for India
# Based on the search results and available data

import pandas as pd
import numpy as np

# Extended India happiness data with additional parameters
india_comprehensive = {
    'Year': list(range(2005, 2025)),
    'Happiness_Score': [None, None, None, None, None, None, 
                        4.98, 4.77, 4.77, 4.57, 4.40, 4.32, 
                        4.19, 4.02, 3.57, 3.82, 3.78, 4.04, 4.05, 4.39],
    'Global_Rank': [None, None, None, None, None, None,
                    None, None, 111, None, 117, 118,
                    None, 133, 144, 144, 139, None, 126, 118],
    'Total_Countries': [None, None, None, None, None, None,
                       None, None, 156, None, 158, 156,
                       155, 156, 156, 153, 149, 146, 137, 147],
}

df_comprehensive = pd.DataFrame(india_comprehensive)

# Calculate percentile rank where available
df_comprehensive['Percentile_from_Bottom'] = None
for idx, row in df_comprehensive.iterrows():
    if pd.notna(row['Global_Rank']) and pd.notna(row['Total_Countries']):
        percentile = (row['Global_Rank'] / row['Total_Countries']) * 100
        df_comprehensive.at[idx, 'Percentile_from_Bottom'] = round(percentile, 1)

print("India's Comprehensive Happiness Data (2005-2024)")
print(df_comprehensive)
print("\n" + "="*70)

# Summary statistics for available data
happiness_scores = df_comprehensive['Happiness_Score'].dropna()
print("\nHappiness Score Statistics:")
print(f"Mean: {happiness_scores.mean():.3f}")
print(f"Median: {happiness_scores.median():.3f}")
print(f"Std Dev: {happiness_scores.std():.3f}")
print(f"Min: {happiness_scores.min():.3f} (Year {df_comprehensive.loc[happiness_scores.idxmin(), 'Year']})")
print(f"Max: {happiness_scores.max():.3f} (Year {df_comprehensive.loc[happiness_scores.idxmax(), 'Year']})")

# Trend Analysis
print("\n" + "="*70)
print("TREND ANALYSIS:")
print(f"2011-2019: Decline from 4.98 to 3.57 (Δ = -1.41 points, -28.3%)")
print(f"2019-2024: Recovery from 3.57 to 4.39 (Δ = +0.82 points, +23.0%)")
print(f"Overall 2011-2024: Decline from 4.98 to 4.39 (Δ = -0.59 points, -11.8%)")

# Save to CSV
df_comprehensive.to_csv('india_happiness_2005_2024.csv', index=False)
print("\n✓ Data saved to: india_happiness_2005_2024.csv")
