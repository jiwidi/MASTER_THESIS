import pandas as pd
from pygnuplot import gnuplot

# Popularity
popularity = pd.read_csv("charts/chart_data/popularity.csv").set_index("rank")

popularity.index.name = "label"
# print(df)
gnuplot.plot_data(
    popularity,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3:xticlabels(1) title columnheader(3) with histograms fs pattern 1",
    xlabel='"Rank"',
    ylabel='"Popularity"',
    yrange="[0:]",
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/popularity.png"',
)


# Ages
ages = pd.read_csv("charts/chart_data/ages.csv").set_index("rank")


ages.index.name = "label"
# print(df)
gnuplot.plot_data(
    ages,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3:xticlabels(1) title columnheader(3) with histograms fs pattern 1",
    xlabel='"Rank"',
    ylabel='"Age (Days)"',
    yrange="[0:]",
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/ages.png"',
)

# Prices
prices = pd.read_csv("charts/chart_data/prices.csv").set_index("rank")

prices.index.name = "label"
gnuplot.plot_data(
    prices,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3:xticlabels(1) title columnheader(3) with histograms fs pattern 1",
    xlabel='"Rank"',
    ylabel='"Price"',
    yrange="[0:]",
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/price.png"',
)
