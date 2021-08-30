import pandas as pd
from pygnuplot import gnuplot
import math

AVG_POP = 963.055035335689
# Popularity
popularity = pd.read_csv("charts/chart_data/popularity.csv").set_index("rank")

popularity.index.name = "label"
popularity["default"] = -50
gnuplot.plot_data(
    popularity,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3 title columnheader(3) with histograms fs pattern 1",
    'using 4:xticlabels(1) title "Average item popularity" with lines lc "red" lw 0.2',
    xlabel='"Item rank"',
    ylabel='"Popularity"',
    yrange="[0:]",
    arrow = f'1 from graph 0, first {AVG_POP} to graph 1, first {AVG_POP} lc "red" lw 2 nohead ',
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/popularity.png"',
)


# Ages
ages = pd.read_csv("charts/chart_data/ages.csv").set_index("rank")

AVG_AGE = 270.2706855791962
ages.index.name = "label"
ages["default"] = -50
# print(df)
gnuplot.plot_data(
    ages,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3:xticlabels(1) title columnheader(3) with histograms fs pattern 1",
    'using 4:xticlabels(1) title "Average item age" with lines lc "red" lw 0.2',
    xlabel='"Item rank"',
    ylabel='"Age (Days)"',
    yrange="[0:]",
    arrow = f'1 from graph 0, first {AVG_AGE} to graph 1, first {AVG_AGE} lc "red" lw 2 nohead ',
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/ages.png"',
)

# Prices
prices = pd.read_csv("charts/chart_data/prices.csv").set_index("rank")
AVG_PRICE = 210.29613299171743
prices.index.name = "label"
prices["default"] = -50
gnuplot.plot_data(
    prices,
    "using 2:xticlabels(1) title columnheader(2) with histograms fs pattern 1",
    "using 3:xticlabels(1) title columnheader(3) with histograms fs pattern 1",
    'using 4:xticlabels(1) title "Average item price" with lines lc "red" lw 0.2',
    xlabel='"Item rank"',
    ylabel='"Price"',
    yrange="[0:]",
    arrow = f'1 from graph 0, first {AVG_PRICE} to graph 1, first {AVG_PRICE} lc "red" lw 2 nohead ',
    terminal='svg standalone fname "Arial bold"',
    term='png medium background "#ffffff"',
    style=["data histogram"],
    output='"charts/price.png"',
)
