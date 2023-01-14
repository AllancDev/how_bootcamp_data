import datetime
import pytest

from apis import DaySummaryApi, TradesApi

class TestDaySummaryApi:

    @pytest.mark.parametrize(
        "coin, date, expected",
        [
            ("BTC", datetime.date(2022, 6, 21), "https://www.mercadobitcoin.net/api/BTC/day-summary/2022/6/21"),
            ("ETH", datetime.date(2022, 6, 21), "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/6/21"),
            ("ETH", datetime.date(2022, 4, 21), "https://www.mercadobitcoin.net/api/ETH/day-summary/2022/4/21"),
        ]
    )
    def test_get_endpoint_api(self, coin, date, expected):
        api = DaySummaryApi(coin=coin)
        actual = api._get_endpoint(date=date)
        
        assert actual == expected


class TestTradesApi:
    @pytest.mark.parametrize(
        "coin, date_from, date_to, expected",
        [
            ("TEST", datetime.datetime(2022, 2, 2), datetime.datetime(2022, 2, 3), 'https://www.mercadobitcoin.net/api/TEST/trades/1643770800/1643857200')
        ]
    )
    def test_get_endpoint(self, coin, date_from, date_to, expected):
        api = TradesApi(coin=coin)
        actual = api._get_endpoint(date_from=date_from, date_to=date_to)
        assert actual == expected
    

    @pytest.mark.parametrize(
        "date, expected",
        [
            (datetime.datetime(2019, 1, 1), int(datetime.datetime(2019, 1, 1).timestamp()))
        ]
    )
    def test_get_unix_epoch(self, date, expected):
        actual = TradesApi(coin="TEST")._get_unix_epoch(date)
        print(actual)
        assert actual == expected
    

