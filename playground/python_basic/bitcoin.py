import pyupbit
import time

access = 'YoUhe50TNVKRjinUYwV3C0P2VCgMnMbarYjcjouV'
secret = 'WUH1k1inPmRTJLRj4cAIjg90pthsvRW5yl3j3kLP'

upbit = pyupbit.Upbit(access, secret)
bitcoinlist = ['KRW-BTC', 'KRW-ETH', 'KRW-ETC', 'KRW-XRP', 'KRW-DOGE', 'KRW-WAVES', 'KRW-SRM', 'KRW-BTT', 'KRW-DAWN', 'KRW-VET', 'KRW-NEO','KRW-ADA', 'KRW-TRX', 'KRW-CHZ']

for bitcoin in bitcoinlist:
  bitcoinohlcv = pyupbit.get_ohlcv(bitcoin, count=1, interval='minute15')
  print('암호화폐', bitcoin, end=" ")
  # print(bitcoinohlcv)
  print('거래량: ', bitcoinohlcv['close'] * bitcoinohlcv['volume'])
  # print(bitcoin, bitcoinohlcv['volume'])
  # bitcoinvolume = bitcoinohlcv['volume']
  # print(bitcoin, bitcoinvolume)