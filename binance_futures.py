import logging
import requests
import pprint

logger = logging.getLogger()

# REST
# Used to place order, cancel order, get status, current balance
# endpoint = "https://fapi.binance.com" # This is the _real_ endpoint, not testnet?
endpoint = "https://testnet.binancefuture.com"

# Websockets
# Used to get live market data
websocket = "wss://fstream.binance.com" # I don't think this is testnet?

def get_contracts():
    response_object = requests.get(endpoint + "/fapi/v1/exchangeInfo")
    print(response_object.status_code)

    contracts = []
    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts


contracts = get_contracts()
print(contracts)