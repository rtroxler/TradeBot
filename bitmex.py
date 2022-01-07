import logging
import requests
import pprint

logger = logging.getLogger()

# REST
# Used to place order, cancel order, get status, current balance
endpoint = "https://testnet.bitmex.com/api/v1"

# Websockets
# Used to get live market data
websocket = ""

def get_contracts():
    response_object = requests.get(endpoint + "/instrument/active")

    contracts = []
    for contract in response_object.json():
        contracts.append(contract['symbol'])

    return contracts


contracts = get_contracts()
print(contracts)
