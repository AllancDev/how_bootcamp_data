import datetime

from mercado_bitcoin.apis import DaySummaryApi


class TestDaySummaryApi:
    def test_get_data(self):
        actual = DaySummaryApi(coin="BTC").get_data(date=datetime.date(2022, 1, 1))
        expected = {
            "date": "2022-01-01",
            "opening": 263989.99999,
            "closing": 267412.0131,
            "lowest": 263732,
            "highest": 269980,
            "volume": "3720079.41498325",
            "quantity": "13.93301257",
            "amount": 2543,
            "avg_price": 266997.49220015,
        }

        assert actual == expected

    def test_get_data_better(self):
        actual = (
            DaySummaryApi(coin="BTC")
            .get_data(date=datetime.date(2022, 1, 1))
            .get("date")
        )
        expected = "2022-01-01"

        assert actual == expected
