import requests
import asyncio
import datetime as dt


def print_binance(symbol): #BTCUSDT
    url = 'https://api.binance.com/api/v1/klines?symbol='+symbol+'&interval=1m'
    data = requests.get(url).json()
    if len(data)>0:
        t = dt.datetime.fromtimestamp(data[-1][0]/1000).strftime("%Y-%m-%dT%H:%M:%SZ")
        p = data[-1][4]
        print(t+' BINANCE '+symbol+' '+p)

def grep_okex_pairs(keyword): #BTC
    r = requests.get('https://www.okex.com/api/futures/v3/instruments/ticker').json()
    list1 = [item['instrument_id'] for item in r if keyword in item['instrument_id']]
    return list1 

def print_okex(symbol):
    now = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    before = (dt.datetime.now()-dt.timedelta(days=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
    arg = {'start':before, 'end':now, 'granularity':'5'}
    data = requests.get('https://www.okex.com/api/futures/v3/instruments/'+symbol+'/candles', params=arg).json()
    if len(data) >0:
        print(data[0][0]+' OKEX '+symbol+' '+data[0][1]+' '+data[0][2]+' '+data[0][3]+' '+data[0][4])

def grep_kraken_pairs(keyword):
    data = requests.get('https://api.kraken.com/0/public/AssetPairs').json()
    dic_data = data['result']
    list1 = [key for key, value in dic_data.items() if keyword in key and '.d' not in key]
    return list1   

def print_kraken(symbol):
    now = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    arg = {'pair': symbol, 'since': now}
    data = requests.get('https://api.kraken.com/0/public/Trades', params=arg).json()
    if len(data['result'][symbol]) > 0:
        p = data['result'][symbol][-1][0]
        t = dt.datetime.fromtimestamp(data['result'][symbol][-1][2]).strftime("%Y-%m-%dT%H:%M:%SZ")
        print(t+' KRAKEN '+symbol+' '+p)

def grep_kraken_futures(keyword): #xbt
    data = requests.get('https://futures.kraken.com/derivatives/api/v3/tickers').json()
    list1 = [ item['symbol'] for item in data['tickers'] if keyword in item['symbol']]
    return list1

def print_kraken_futures(symbol): #'pi_xbtusd'
    now = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
    arg = {'symbol': symbol, 'lastTime': now}
    data = requests.get('https://futures.kraken.com/derivatives/api/v3/history', params=arg).json()
    if len(data['history']) >0 :
        dic = data['history'][0]
        print(dic['time']+' KRAKEN '+symbol+' '+str(dic['price']))

def grep_bitmex_pairs(keyword):
    data = requests.get('https://www.bitmex.com/api/v1/instrument/active').json()
    list1 = [item['symbol'] for item in data if keyword in item['symbol']]
    list1.append('.BXBT')
    list1.append('.BXBT30M')
    list1.append('.XBTUSDPI8H')
    return list1

def print_bitmex(symbol): 
    arg = {'symbol': symbol, 'count':'20', 'columns':'price', 'reverse':'true'}
    data = requests.get('https://www.bitmex.com/api/v1/trade', params=arg).json()
    if len(data) > 0:
        dic = data[0]
        print(dic['timestamp']+' BITMEX '+symbol+' '+str(dic['price']))

async def periodic():
    while True:
        now = dt.datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')
        print("----------------------")
        print("now: "+ now)
        instrs = grep_okex_pairs('BTC')
        for instr in instrs:
            print_okex(instr)

        instrs = grep_kraken_pairs('XXBT')
        for instr in instrs:
            print_kraken(instr)
        
        instrs = grep_kraken_futures('xbt')
        for instr in instrs:
            print_kraken_futures(instr)
        
        instrs = grep_bitmex_pairs('XBT')
        for instr in instrs:
            print_bitmex(instr)
        print_binance('BTCUSDT')
        await asyncio.sleep(60)

def stop():
    task.cancel()

loop = asyncio.get_event_loop()
#loop.call_later(3*24*60*60, stop)
task = loop.create_task(periodic())

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass

