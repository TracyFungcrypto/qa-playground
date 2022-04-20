import json

import pytest as pytest
import requests

r = requests.get('https://api.crypto.com/v2/public/get-instruments')
r_dict = json.loads(r.text)


class Instrument:
    def __init__(
            self,
            instrument_name,
            quote_currency,
            base_currency,
            price_decimals,
            quantity_decimals,
            margin_trading_enabled,
            margin_trading_enabled_5x,
            margin_trading_enabled_10x,
            max_quantity,
            min_quantity
    ):
        self.instrument_name = instrument_name
        self.quote_currency = quote_currency
        self.base_currency = base_currency
        self.price_decimals = price_decimals
        self.quantity_decimals = quantity_decimals
        self.margin_trading_enabled = margin_trading_enabled
        self.margin_trading_enabled_5x = margin_trading_enabled_5x
        self.margin_trading_enabled_10x = margin_trading_enabled_10x
        self.max_quantity = max_quantity
        self.min_quantity = min_quantity


instruments = []
for item in r_dict['result']['instruments']:
    instrument = Instrument(item["instrument_name"],
                            item["quote_currency"],
                            item["base_currency"],
                            item["price_decimals"],
                            item["quantity_decimals"],
                            item["margin_trading_enabled"],
                            item["margin_trading_enabled_5x"],
                            item["margin_trading_enabled_10x"],
                            item["max_quantity"],
                            item["min_quantity"])
    instruments.append(instrument)


def search(instrument_name):
    for i in instruments:
        if i.instrument_name == instrument_name:
            return i


@pytest.mark.parametrize(
    "insturment_name, price_decimals, quantity_decimals, margin_trading_enabled, margin_trading_enabled_5x,margin_trading_enable_10x, max_quantity, min_quantity",
    [["BTC_USDT", 2, 6, True, True, True, "10000", "0.000001"],
     ["ETH_USDT", 2, 5, True, True, True, "100000", "0.00001"],
     ["CRO_USDT", 5, 3, True, True, True, "10000000", "0.001"],
     ["ALI_USDT", 6, 0, False, False, False, "251000", "1"]])
def test_is_correct(insturment_name, price_decimals, quantity_decimals, margin_trading_enabled,
                    margin_trading_enabled_5x, margin_trading_enable_10x, max_quantity, min_quantity):
    i = search(insturment_name)
    assert i.price_decimals == price_decimals
    assert i.quantity_decimals == quantity_decimals
    assert i.margin_trading_enabled == margin_trading_enabled
    assert i.margin_trading_enabled_5x == margin_trading_enabled_5x
    assert i.margin_trading_enabled_10x == margin_trading_enable_10x
    assert i.max_quantity == max_quantity
    assert i.min_quantity == min_quantity
