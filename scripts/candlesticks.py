from bootstrap import bootstrap
bootstrap()

from kalshi.api import get_candlesticks
from transforms.dates import make_date

if __name__ == '__main__':

    while True:

        print('This is a REPL (Read-Execute-Print-Loop) environment')
        print('Please name a kalshi contract, start date, and end date')
        print('The program will compute statistics about this market over the timeframe')

        doBreak = input('Use the hardcoded example? Y or N:\t').strip()
        if doBreak.upper() == 'Y': break

        # get a ticker
        ticker = input('Kalshi ticker name:\t\t').strip()

        # loop until valid date input
        start = input('Start date (DD-MM-YYYY):\t').strip()
        while start.count('/') != 2 and len(start) != 10:
            start = input('Start date (DD-MM-YYYY):\t').strip()

        # loop until valid date input
        end = input('End date (DD-MM-YYYY):\t\t').strip()
        while end.count('/') != 2 and len(end) != 10:
            end = input('End date (DD-MM-YYYY):\t\t').strip()

        # parse dates
        start = make_date(*(d for d in start.split('-')), True)
        end = make_date(*(d for d in end.split('-')), True)

        # send the api call
        data = get_candlesticks(ticker, start, end, granularity='1d')
        print(data)
        print(f'Found {len(data['candlesticks'])} results')

    # market for fed decision in december 2025
    ticker = 'KXFEDDECISION-25DEC-H0'
    start = '01-11-2025'
    end = '01-12-2025'

    start = make_date(*(d for d in start.split('-')), True)
    end = make_date(*(d for d in end.split('-')), True)
    data = get_candlesticks(ticker, start, end, granularity='1h')

    from transforms.kalshi import to_simple_df
    ohlc = to_simple_df(data)
    print(ohlc)

    print('na value count:')
    print(ohlc.isna().sum())
    
    # making a plot of the data
    from charts.candlesticks import moving_price
    moving_price(ohlc)

    from misc.plotting import plot_img_in_terminal
    plot_img_in_terminal('./charts/imgs/moving_average.png')