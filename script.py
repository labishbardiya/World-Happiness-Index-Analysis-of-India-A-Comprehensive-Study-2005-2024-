
# Let me compile the India happiness data from 2005-2024 based on the search results
import pandas as pd
import numpy as np

# Creating India's happiness data from the sources
# Source: web:19, web:57, web:63, web:64, web:56, web:59, web:21, web:26

india_data = {
    'Year': [2005, 2006, 2007, 2008, 2009, 2010, 
             2011, 2012, 2013, 2014, 2015, 2016, 
             2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Happiness_Score': [
        None, None, None, None, None, None,  # 2005-2010 no specific data found
        4.98, 4.77, 4.77, 4.57, 4.40, 4.32,  # Based on web:57
        4.19, 4.02, 3.57, 3.82, 3.78, 4.04, 4.05, 4.39  # Based on web:19, web:57
    ],
    'Rank': [
        None, None, None, None, None, None,
        None, None, 111, None, 117, 118,  # Based on web:56, web:59
        None, 133, 144, 144, 139, None, 126, 118  # Based on web:63, web:64, web:21
    ],
    'Total_Countries': [
        None, None, None, None, None, None,
        None, None, 156, None, 158, 156,
        155, 156, 156, 153, 149, 146, 137, 147
    ]
}

df_india = pd.DataFrame(india_data)
print("India's Happiness Data (2005-2024)")
print(df_india)
print("\n")
print("Data Summary:")
print(f"Available Happiness Scores: {df_india['Happiness_Score'].notna().sum()} years")
print(f"Available Rankings: {df_india['Rank'].notna().sum()} years")
