# World Happiness Index — India (2005–2024)

A analysis and visualization project that collects and visualizes India's World Happiness data across 2005–2024. The repository contains the processed data, plotting scripts (Plotly), and generated plots comparing India's happiness score and global rank over time.

## Contents

- `india_happiness_2005_2024.csv` — primary dataset used for analysis (years 2005–2024). Columns include Year, Happiness_Score, Global_Rank, Total_Countries, Percentile_from_Bottom.
- `happiness_indicators_description.csv` — descriptions of the indicators used in the dataset.
- `india_performance_periods.csv` — (additional breakdowns / period definitions used in the analysis).
- `problem_statements_objectives.csv` — project objectives and problem statements.
- `chart_script.py` — creates a line chart of India's happiness score (2011–2024) with a fitted linear trend; saves `happiness_chart.png` and `happiness_chart.svg` and displays the interactive figure.
- `chart_script_1.py` — produces a bar chart comparing India with the top-5 happiest countries (2024); saves `happiness_comparison.png` and `happiness_comparison.svg`.
- `chart_script_2.py` — scatter chart of Happiness Score vs Global Rank (with years annotated) and a trend line; saves `chart.png` and `chart.svg`.
- `script.py` — constructs and prints a small DataFrame summarizing India's happiness score and rank across years (used to prepare/validate the data).
- `plots/` — directory with additional pre-generated plots (e.g. `gdp_vs_happiness_IND_2011_2024.png`, `social_support_distribution_2024.png`).

## Summary of what the scripts do

- `chart_script.py`
	- Reads in the in-script data (2011–2024), fits a linear regression trend (scikit-learn), and produces an interactive Plotly line chart.
	- Saves raster/vector images using Plotly's image export (requires `kaleido` or `orca`).

- `chart_script_1.py`
	- Builds a small comparison bar chart between India and the top-5 happiest countries for 2024, applying custom colors and text annotations.

- `chart_script_2.py`
	- Creates a scatter of Happiness Score vs Global Rank with year labels and an overlaid polynomial trend line; inverts the y-axis so better ranks (lower numbers) appear at the top.

- `script.py`
	- Assembles the India time-series dataset into a pandas DataFrame and prints a simple summary to the console. Useful as an ETL sanity check.

## Requirements

The scripts are written for Python 3.8+ and rely on a small set of common data/plotting libraries.

Suggested minimal requirements (create a `requirements.txt`):

```
pandas
numpy
plotly
scikit-learn
kaleido
```

Notes:
- Plot image export (e.g., `fig.write_image(...)`) requires `kaleido` (recommended) or `orca` to be installed. Installing `kaleido` via pip is the easiest option.

## How to run

1. Create and activate a Python virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # or install the packages listed in Requirements
```

2. Run a script to generate plots. Examples:

```bash
python chart_script.py      # generates happiness_chart.png, happiness_chart.svg and displays the chart
python chart_script_1.py    # generates happiness_comparison.png/.svg
python chart_script_2.py    # generates chart.png/.svg
python script.py            # prints the assembled DataFrame summary
```

3. Outputs are saved in the repository root (PNG/SVG) and some additional plots are stored in `plots/`.

