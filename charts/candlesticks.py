import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import StrMethodFormatter


def moving_price(data: pd.DataFrame, window: int = 24):
    '''
    Plots the moving average of the candlestick average price over time.

    data is the simple dataframe from transforms.kalshi.to_simple_df, with columns:
    - ts (unix timestamp)
    - average (mean of open/high/low/close, in dollars)

    window is the number of candlesticks in the rolling mean (24 = one day of hourly candles).
    Candlesticks with no price (NaN) are skipped inside each window.
    '''

    df = data.sort_values('ts')

    # unix timestamps -> timezone-aware datetimes so matplotlib treats the x axis as dates
    times = pd.to_datetime(df['ts'], unit='s', utc=True)
    moving_avg = df['average'].rolling(window=window, min_periods=1).mean()

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(times, moving_avg, color='#2a78d6', linewidth=2)

    # x axis: dates
    locator = mdates.AutoDateLocator()
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.ConciseDateFormatter(locator))
    ax.set_xlabel('Date (UTC)')

    # y axis: dollars
    ax.yaxis.set_major_formatter(StrMethodFormatter('${x:,.2f}'))
    ax.set_ylabel('Average price')

    ax.set_title(f'{window}-period moving average price')

    # keep grid and frame recessive so the line carries the chart
    ax.grid(axis='y', color='#e5e4e0', linewidth=0.8)
    ax.set_axisbelow(True)
    for side in ('top', 'right'):
        ax.spines[side].set_visible(False)

    fig.tight_layout()

    plot_name = 'moving_average.png'
    image_path = f'./charts/imgs/{plot_name}'
    plt.savefig(image_path, format="png", bbox_inches="tight")
    plt.close()

    return fig, ax
