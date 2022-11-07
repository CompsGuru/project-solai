import json
from decouple import config
from aiohttp import ClientSession
from channels.layers import get_channel_layer
from stocks.models import Stock


class StocksController:
    @classmethod
    def create_stocks(cls, data):
        cls.logger(f"Creating {len(data['stocks'])} stock(s)...")
        instances = [Stock(**stock) for stock in data]
        stocks = Stock.create_stocks(instances)
        print("Created: ", len(stocks))

    @classmethod
    def update_stocks(cls, data):
        cls.logger(f"Updating {len(data['stocks'])} stock(s)...")
        stocks = cls.send_request("PUT", data, "Updated")
        return stocks

    @classmethod
    def send_request(cls, method, data, operation, **kwargs):
        with ClientSession() as session:
            resp = session.request(
                method=method, url=cls.url, json=data, **kwargs)
            resp.raise_for_status()
            stocks = json.loads(resp.text())
            cls.logger(
                f"{operation} {len(stocks['stocks'])} stock(s)\n")
            return stocks

    def update_clients(stock):
        channel_layer = get_channel_layer()
        channel_layer.group_send(
            "stock_clients",
            {"type": "client_message", "data": stock}
        )

    def logger(text):
        return print(f"\n::: {text}", end="")
