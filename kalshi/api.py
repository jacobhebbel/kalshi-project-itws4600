import datetime
import requests

def send_request(url, method, query: dict, headers=None, returnRaw=False):
    '''
    Sends the API call, logs if the message had a 4xx or 5xx
    '''

    # check if headers are needed for this request
    if headers is None:
        protected = ['/portfolio', '/apikeys']
        if any(p in url for p in protected):
            raise ValueError('ERROR: Request to protected Kalshi endpoint missing headers')

    response = None
    match method.upper():
        case 'GET': response = requests.get(url, params=query, headers=headers)
        case 'POST': response = requests.post(url, params=query,headers=headers)
        case _: raise RuntimeError(f'ERROR: support not implemented for method {method.upper()}')

    if response.status_code >= 400:
        print(f'ERROR: Response object had status {response.status_code}')

    data = response.json()
    if data is None: data = response.text
    return data

def get_candlesticks(ticker: str, start: datetime.datetime, finish: datetime.datetime, granularity: str = '1m'):
    '''
    Makes an API call that fetches candlestick data from start to finish at a specific granularity
    ticker          - a KX ticker name
    start           - an ISO date string
    finish          - an ISO date string
    granularity     - one of [1m, 5m,  30m, 1h, 6h, 12h, 1d]
    '''

    # check that dates are Datetime objects
    # checkthat start < finish
    # check that granularity is valid
    
    if start >= finish: raise ValueError('ERROR: start happens after finish')
    if granularity not in ['1m', '1h', '1d']: raise ValueError('ERROR: Illegal granularity argument')

    # convert granularity
    g_int = None
    match granularity:
        case '1m': g_int = 1
        case '1h': g_int = 60
        case '1d': g_int = 1440

    # define request variables (URL, query args, key object)
    # use a requests object to send a request to Kalshi API
    # validate the response status, response shape
    # log the request and response
    # send the data 

    url = f'https://external-api.kalshi.com/trade-api/v2'
    endpoint = f'/historical/markets/{ticker}/candlesticks'
    query = { 'start_ts': int(start.timestamp()), 'end_ts': int(finish.timestamp()), 'period_interval': g_int }
    method = 'get'

    print(url)
    print(endpoint)
    print(query)
    print(method)

    url += endpoint
    data = send_request(url, method, query)
    return data

