import pandas as pd

PRICE_COLS = ['open', 'high', 'low', 'close', 'average']

def to_simple_df(raw: dict):
    '''
    Returns a DF of Timestamp - Open - High - Low - Close - Average
    Prices are parsed to floats. Average is Kalshi's price.mean for the period.
    Periods with no trades (all prices null) are filled with price.previous,
    the last traded price; if that is also missing the row stays NaN.
    '''

    simple = []
    for stick in raw['candlesticks']:
        price = stick['price']
        row = {'open': price['open'], 'close': price['close'], 'high': price['high'], 'low': price['low'], 'average': price['mean'], 'ts': stick['end_period_ts']}

        # no trades this period -> carry the last traded price
        if price['open'] is None:
            for col in PRICE_COLS:
                row[col] = price.get('previous')

        simple.append(row)

    df = pd.DataFrame(simple)
    df[PRICE_COLS] = df[PRICE_COLS].apply(pd.to_numeric, errors='coerce').astype(float)
    return df
