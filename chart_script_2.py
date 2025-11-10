import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Data
data = {
    "Year": [2013, 2015, 2016, 2018, 2019, 2020, 2021, 2023, 2024],
    "Happiness_Score": [4.77, 4.40, 4.32, 4.02, 3.57, 3.82, 3.78, 4.05, 4.39],
    "Global_Rank": [111, 117, 118, 133, 144, 144, 139, 126, 118]
}

df = pd.DataFrame(data)

# Create scatter plot
fig = go.Figure()

# Add scatter points
fig.add_trace(go.Scatter(
    x=df['Happiness_Score'],
    y=df['Global_Rank'],
    mode='markers+text',
    text=df['Year'],
    textposition='top center',
    marker=dict(
        size=10,
        color='#1FB8CD',
        line=dict(width=2, color='white')
    ),
    name='India Data',
    showlegend=False
))

# Calculate and add trend line
z = np.polyfit(df['Happiness_Score'], df['Global_Rank'], 1)
p = np.poly1d(z)
x_trend = np.linspace(df['Happiness_Score'].min(), df['Happiness_Score'].max(), 100)
y_trend = p(x_trend)

fig.add_trace(go.Scatter(
    x=x_trend,
    y=y_trend,
    mode='lines',
    line=dict(color='#DB4545', width=2, dash='dash'),
    name='Trend Line',
    showlegend=False
))

# Update layout
fig.update_layout(
    title="India's Happiness Score vs Global Ranking",
    xaxis_title="Happiness Score",
    yaxis_title="Global Rank (Lower is Better)"
)

# Invert Y-axis so lower ranks appear at top
fig.update_yaxes(autorange='reversed')

# Update traces for professional styling
fig.update_traces(cliponaxis=False)

# Save as PNG and SVG
fig.write_image("chart.png")
fig.write_image("chart.svg", format="svg")

print("Chart saved successfully as chart.png and chart.svg")