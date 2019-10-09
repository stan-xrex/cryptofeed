from cryptofeed.standards import *
from cryptofeed.pairs import *
from cryptofeed.exchanges import *



kraken_syms = kraken_pairs()
bitmex_syms = Bitmex.get_active_symbols()
kraken_future_syms = kraken_future_pairs()
bitfinex_syms = bitfinex_pairs()
bitstamp_syms = bitstamp_pairs()
okcoin_syms = okcoin_pairs()
okex_syms = okex_pairs()
binance_syms = binance_pairs()
coinbase_syms = coinbase_pairs()
poloniex_syms = poloniex_pairs() 
gemini_syms = gemini_pairs()
hitbtc_syms = hitbtc_pairs()

#kraken_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
#        'ADA-ETH', 'EOS-ETH', 'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']
#
#bitfinex_syms = ['ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC', 'EOS-ETH',
#        'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']
#bitstamp_syms = ['ETH-BTC', 'LTC-BTC', 'XRP-BTC']
##okcoin_syms = ['ETH-BTC', 'LTC-BTC', 'XRP-BTC']
##okex_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
##        'ADA-ETH', 'EOS-ETH', 'LTC-ETH', 'BTC-USD', 'ETH-USD', 'LTC-USD', 'EOS-USD']
#binance_syms = ['ADA-BTC', 'DASH-BTC', 'ETH-BTC', 'EOS-BTC', 'LTC-BTC', 'XLM-BTC', 'XMR-BTC', 'XRP-BTC', 'ZEC-BTC',
#        'ADA-ETH', 'EOS-ETH', 'LTC-ETH']

print("kraken:\n", kraken_syms)
print("kraken_future:\n", kraken_future_syms)
print("bitmex:\n", bitmex_syms)
print("bitfinex:\n", bitfinex_syms)
print("bitstamp:\n", bitstamp_syms)
print("okcoin:\n", okcoin_syms)
print("okex:\n", okex_syms)
print("binance:\n", binance_syms)
print("coinbase:\n", coinbase_syms)
print("poloniex:\n", poloniex_syms)
print("gemini:\n", gemini_syms)
print("hitbtc:\n", hitbtc_syms)




