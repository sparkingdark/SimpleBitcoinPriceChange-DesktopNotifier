import requests
import json
import time

from notify import Notify

def getBitcoinPrice():
    BTC_API_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    response_json = requests.get(BTC_API_URL).json()

    updatetime = response_json['time']['updated']
    btcrate = response_json['bpi']['USD']['rate']
    return {
        'time' : updatetime,
        'rate' : btcrate
    }

def log(time, rate):
    with open('log.txt','a+') as file:
        file.write(
            "Timestamp: " + time + '\n' +
            "USD Rate: $" + rate + '\n' +
            (4* '------') + '\n'
        )

    file.close()


# Var
previous = {
    'time' : '',
}

while True:
    current = getBitcoinPrice()

    if (current['time'] != previous['time']) :
        Notify.ping(current['rate'])
        log(current['time'], current['rate'])
        previous['time'] = current['time']

    time.sleep(30) #seconds