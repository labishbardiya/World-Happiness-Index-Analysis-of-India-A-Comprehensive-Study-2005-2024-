
# Create comprehensive data table for the report including available indicators
import pandas as pd
import numpy as np

# Create detailed summary table for problem statements and objectives
problem_objectives_data = {
    'Problem Statement': [
        'PS1: Trend of India\'s Happiness Index (2005-2024)',
        'PS2: Relationship between GDP and Happiness Score',
        'PS3: Role of Social Support and Life Expectancy',
        'PS4: Comparative analysis with top-ranked countries'
    ],
    'Objective 1': [
        'O1.1: Analyze year-on-year trend in happiness score',
        'O2.1: Determine correlation between GDP per capita and happiness',
        'O3.1: Examine impact of social support on happiness score',
        'O4.1: Compare India with top 5 happiest countries'
    ],
    'Objective 2': [
        'O1.2: Identify factors contributing to rank fluctuations',
        'O2.2: Assess whether economic growth translates to happiness',
        'O3.2: Analyze role of healthy life expectancy',
        'O4.2: Identify gaps and areas for improvement'
    ]
}

df_ps_obj = pd.DataFrame(problem_objectives_data)
print("PROBLEM STATEMENTS AND OBJECTIVES")
print("="*100)
print(df_ps_obj.to_string(index=False))
print("\n\n")

# Create comprehensive data overview
# Based on search results, create a summary of key factors
factors_data = {
    'Indicator': [
        'Happiness Score',
        'GDP per Capita',
        'Social Support',
        'Healthy Life Expectancy',
        'Freedom to Make Choices',
        'Generosity',
        'Perception of Corruption'
    ],
    'Description': [
        'Average life evaluation on 0-10 scale (Cantril Ladder)',
        'Log GDP per capita from World Bank data',
        'Having someone to count on in times of trouble',
        'Healthy years expected at birth from WHO',
        'Satisfaction with freedom to choose life direction',
        'Charity donations and helping strangers',
        'Absence of corruption in government and business'
    ],
    'India_2024_Status': [
        '4.39 (Score), 118th rank',
        'Lower-middle income group',
        'Ranked 141st globally',
        '67.3 years (2021 data)',
        'Ranked 23rd in 2024',
        'Ranked 57th for donations, 10th for volunteering',
        'Ranked 96th (CPI score: 38/100)'
    ],
    'Importance': [
        'Primary measure of subjective well-being',
        'Explains 31% of happiness variation',
        'Explains 26% of happiness variation',
        'Significant predictor of life satisfaction',
        'Strong predictor of happiness',
        'Positive impact on giver and receiver',
        'Trust in institutions affects social cohesion'
    ]
}

df_factors = pd.DataFrame(factors_data)
print("KEY INDICATORS OF WORLD HAPPINESS INDEX")
print("="*100)
print(df_factors.to_string(index=False))
print("\n\n")

# India's performance summary by year groups
periods_data = {
    'Period': ['2011-2013', '2014-2016', '2017-2019', '2020-2022', '2023-2024'],
    'Avg_Score': [4.84, 4.43, 3.93, 3.88, 4.22],
    'Best_Rank': [111, 117, 133, 139, 118],
    'Worst_Rank': [111, 118, 144, 144, 126],
    'Trend': ['High baseline', 'Gradual decline', 'Sharp decline', 'Recovery begins', 'Continued improvement'],
    'Key_Events': [
        'Early data collection',
        'Economic reforms ongoing',
        'Economic slowdown, COVID impact',
        'Post-pandemic recovery',
        'Economic growth acceleration'
    ]
}

df_periods = pd.DataFrame(periods_data)
print("INDIA'S HAPPINESS PERFORMANCE BY PERIOD")
print("="*100)
print(df_periods.to_string(index=False))
print("\n\n")

# Save all tables to CSV for potential inclusion
df_ps_obj.to_csv('problem_statements_objectives.csv', index=False)
df_factors.to_csv('happiness_indicators_description.csv', index=False)
df_periods.to_csv('india_performance_periods.csv', index=False)

print("✓ All summary tables saved as CSV files")
