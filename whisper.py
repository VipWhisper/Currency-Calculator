from requests import get, post as whisper
from os import system
system('cls')
system('clear')

crypto = input('[+] Crypto Currency (ETH/BTC/USDT...): ')
currency = input('[+] Currency (USD/EURO/RUB...): ')
print('='*50)
res = whisper(f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms={currency}', headers={"Host": "min-api.cryptocompare.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/4.9.2"}).json()
try:
  previous_price = float(str(res).split(': ')[1].split('}')[0])
  print(f'[=] Fixed Amount : 1 {crypto} = {previous_price} {currency}')
  print('='*50)
  while True:
   res2 = whisper(f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms={currency}', headers={"Host": "min-api.cryptocompare.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/4.9.2"}).json()
   price=float(str(res2).split(': ')[1].split('}')[0])
   percentage_change = ((price - previous_price) / previous_price) * 100
   difference = price - previous_price
   print(f'[=] 1 {crypto} = {price} {currency} | {difference} / {percentage_change} %')
except:
   exit(res)