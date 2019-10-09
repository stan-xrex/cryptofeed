from cryptofeed.feedhandler import FeedHandler
from cryptofeed.callback import TickerCallback, TradeCallback, BookCallback, FundingCallback
from cryptofeed import FeedHandler
from cryptofeed.exchanges import Bitmex, Coinbase, Bitfinex, Poloniex, Gemini, HitBTC, Bitstamp, Kraken, Binance, EXX, Huobi, HuobiUS, OKCoin, OKEx, Coinbene
from cryptofeed.defines import L3_BOOK, L2_BOOK, BID, ASK, TRADES, TICKER, FUNDING, COINBASE

from cryptofeed.standards import *
import asyncio

async def book(feed, pair, book, timestamp):

    bidstr = "Bid:"
    for k, v in book[BID].items():
        bidstr = bidstr + " " +str(k)+" "+str(v)
    askstr = "Ask:"
    for k, v in book[ASK].items():
        askstr = askstr + " "+str(k)+" "+str(v)

    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} {bidstr}')
    print(f'Timestamp: {timestamp} Feed: {feed} Pair: {pair} {askstr}')


kraken_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
        'ADA-ETH', 'EOS-ETH', 'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']

bitfinex_syms = ['ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC', 'EOS-ETH',
        'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']
bitstamp_syms = ['ETH-BTC', 'LTC-BTC', 'XRP-BTC']
binance_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
        'ADA-ETH', 'EOS-ETH', 'LTC-ETH']
fh = FeedHandler()




fh.add_feed(Kraken(pairs=kraken_syms, channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
#fh.add_feed(Bitfinex(pairs=bitfinex_syms, channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
#fh.add_feed(Bitstamp(pairs=bitstamp_syms, channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))
fh.add_feed(Binance(pairs=binance_syms, channels=[L2_BOOK], callbacks={L2_BOOK: BookCallback(book)}))



fh.run()

