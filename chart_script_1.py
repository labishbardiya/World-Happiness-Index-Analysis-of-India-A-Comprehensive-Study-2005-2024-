import plotly.graph_objects as go
import pandas as pd

# Create the data
data = {
    "Country": ["Finland", "Denmark", "Iceland", "Sweden", "Netherlands", "India"],
    "Happiness_Score": [7.736, 7.521, 7.515, 7.345, 7.306, 4.389],
    "Category": ["Top 5", "Top 5", "Top 5", "Top 5", "Top 5", "India"]
}

df = pd.DataFrame(data)

# Create color mapping
colors = []
for category in df['Category']:
    if category == "Top 5":
        colors.append('#2E8B57')  # Sea green for top 5
    else:
        colors.append('#DB4545')  # Bright red for India

# Create the bar chart
fig = go.Figure(data=[
    go.Bar(
        x=df['Country'],
        y=df['Happiness_Score'],
        marker_color=colors,
        text=[f"{score:.3f}" for score in df['Happiness_Score']],
        textposition='outside',
        textfont=dict(size=12),
        cliponaxis=False
    )
])

# Update layout
fig.update_layout(
    title="India vs Top 5 Happiest Countries 2024",
    xaxis_title="Country",
    yaxis_title="Happiness Score",
    yaxis=dict(range=[0, 8]),
    showlegend=False
)

# Update traces for professional appearance
fig.update_traces(cliponaxis=False)

# Save the chart as both PNG and SVG
fig.write_image("happiness_comparison.png")
fig.write_image("happiness_comparison.svg", format="svg")