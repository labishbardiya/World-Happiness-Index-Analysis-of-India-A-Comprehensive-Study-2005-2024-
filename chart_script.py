import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

# Data from the provided JSON
data = {
    "Year": [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Happiness_Score": [4.98, 4.77, 4.77, 4.57, 4.40, 4.32, 4.19, 4.02, 3.57, 3.82, 3.78, 4.04, 4.05, 4.39]
}

df = pd.DataFrame(data)

# Create figure
fig = go.Figure()

# Add the main line chart
fig.add_trace(go.Scatter(
    x=df['Year'],
    y=df['Happiness_Score'],
    mode='lines+markers',
    name='Happiness Score',
    line=dict(width=3),
    marker=dict(size=8),
    hovertemplate='Year: %{x}<br>Score: %{y:.2f}<extra></extra>'
))

# Calculate and add trend line
X = df['Year'].values.reshape(-1, 1)
y = df['Happiness_Score'].values
model = LinearRegression()
model.fit(X, y)
trend_y = model.predict(X)

fig.add_trace(go.Scatter(
    x=df['Year'],
    y=trend_y,
    mode='lines',
    name='Trend',
    line=dict(dash='dash', width=2),
    hovertemplate='Year: %{x}<br>Trend: %{y:.2f}<extra></extra>'
))

# Update layout
fig.update_layout(
    title="India's Happiness Score Trend (2011-2024)",
    xaxis_title="Year",
    yaxis_title="Happiness Score",
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Set Y-axis range and update axes
fig.update_yaxes(range=[3.0, 5.5])
fig.update_xaxes(dtick=1)

# Update traces for better appearance
fig.update_traces(cliponaxis=False)

# Save as both PNG and SVG
fig.write_image("happiness_chart.png")
fig.write_image("happiness_chart.svg", format="svg")

fig.show()