from cryptofeed.feedhandler import FeedHandler
from cryptofeed.callback import TickerCallback, TradeCallback, BookCallback, FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitmex, Coinbase, Bitfinex, Poloniex, Gemini, HitBTC, Bitstamp, Kraken, Binance, EXX, Huobi, HuobiUS, OKCoin, OKEx, Coinbene
from cryptofeed.defines import L3_BOOK, L2_BOOK, BID, ASK, TRADES, TICKER, FUNDING, COINBASE

from cryptofeed.standards import *
import asyncio

def nbbo_ticker(pair, bid, ask, bid_feed, ask_feed):
    print('Pair: {} Bid: {} Bid Feed: {} Ask: {} Ask Feed: {}'.format(pair,
                                                                      bid,
                                                                      bid_feed,
                                                                      ask,
                                                                      ask_feed))


async def ticker(feed, pair, bid, ask):
    print(f'Feed: {feed} Pair: {pair} Bid: {bid} Ask: {ask}')


async def trade(feed, pair, order_id, timestamp, side, amount, price):
    print(f"Timestamp: {timestamp} Feed: {feed} Pair: {pair} ID: {order_id} Side: {side} Amount: {amount} Price: {price}")


async def book(feed, pair, book, timestamp):

    bidstr = "Bid:"
    for k, v in book[BID].items():
        bidstr = bidstr + " " +str(k)+" "+str(v)
    askstr = "Ask:"
    for k, v in book[ASK].items():
        askstr = askstr + " "+str(k)+" "+str(v)

    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} {bidstr}')
    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} {askstr}')

async def funding(**kwargs):
    print(f"Funding Update for {kwargs['feed']}")
    print(kwargs)

kraken_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
        'ADA-ETH', 'EOS-ETH', 'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']

bitfinex_syms = ['ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC', 'EOS-ETH',
        'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']
bitstamp_syms = ['ETH-BTC', 'LTC-BTC', 'XRP-BTC']
binance_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
        'ADA-ETH', 'EOS-ETH', 'LTC-ETH']

okcoin_syms = ['BTC-USD', 'LTC-USD', 'ETH-USD', 'ETC-USD', 'TUSD-USD', 'USDT-USD', 'ZEC-USD', 'ADA-USD', 'XLM-USD', 'ZRX-USD', 'XRP-USD']
okex_syms = ['BTC-USD-SWAP', 'BTC-USD-190607']
fh = FeedHandler()




#fh.add_feed(Kraken(channels=[TRADES], pairs=kraken_syms, callbacks={TRADES: TradeCallback(trade)}))
#fh.add_feed(Bitfinex(channels=[TRADES], pairs=bitfinex_syms, callbacks={TRADES: TradeCallback(trade)}))
#fh.add_feed(Bitstamp(channels=[TRADES], pairs=bitstamp_syms, callbacks={TRADES: TradeCallback(trade)}))
#fh.add_feed(Binance(channels=[TRADES], pairs=binance_syms, callbacks={TRADES: TradeCallback(trade)}))
fh.add_feed(OKEx(channels=[TRADES], pairs=okex_syms, callbacks={TRADES: TradeCallback(trade)}))




fh.run()

