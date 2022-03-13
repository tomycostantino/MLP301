# Tomas Costantino A00042881

from binance.client import Client
import datetime as dt
import pandas as pd
import numpy as np
import csv


timeframe = {
            '1m': Client.KLINE_INTERVAL_1MINUTE,
            '5m': Client.KLINE_INTERVAL_5MINUTE,
            '15m': Client.KLINE_INTERVAL_15MINUTE,
            '30m': Client.KLINE_INTERVAL_30MINUTE,
            '1h': Client.KLINE_INTERVAL_1HOUR
            }


def get_candlesticks(client: Client, asset: str, interval: str):
    """Get all the klines from api"""

    bars = client.get_historical_klines(asset.upper(), timeframe[interval], '1 Jan, 2020')

    # delete unwanted data - just keep date, open, high, low, close and volume
    for line in bars:
        del line[6:]

    df = pd.DataFrame(bars, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    df['date'] = pd.to_datetime(df['date'], unit='ms')
    df.set_index('date', inplace=True)

    df.to_csv(f'{asset.lower()}_{interval}.csv', sep=',')


if __name__ == '__main__':

    api_key = '5CWQHvHfhyU9WWWWiRUaY0xbq6wmQkgO4512GKupzTkrwwdiTphQQxsZQCcB48rM'
    api_secret = 'ULgitDDFVLA9RELEXA8nisOUZLi9JVWUZPsKs3ctjMj2iszmMDdx5Kmeg8sz5xik'

    client = Client(api_key, api_secret)

    get_candlesticks(client, 'BTCUSDT', '30m')
