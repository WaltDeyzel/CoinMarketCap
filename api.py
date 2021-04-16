from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
import operator
from display import DisplayData
from coinData import CoinData

class CryptoData:
  def getData(self):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':'200',
      'convert':'ZAR'
    }
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': '96e23a7b-6435-46a1-9588-ae3dd3a1b753',
    }

    session = Session()
    session.headers.update(headers)
   
    #STORE ALL THE CRUPTO DATA IN DATA LIST
    data = []
    #SPESIFIC COINS 
    wallet = ['BTC', 'GNT', 'ETH', 'ADA', 'CVC', 'OMG', 'ZEC', 'XRP', 'LTC', 'LSK', 'NEO', 'XMR', 'QTUM', "DOT", "THETA", "DASH"] 
    bitcoin_marketcap = 0

    try:
      response = session.get(url, params=parameters)
      data1 = json.loads(response.text)
      print(type(data1['data'][0]['quote']['ZAR']['percent_change_90d']))
      for coin in data1['data']:
        
        no   = coin['cmc_rank']
        name  = coin['name'].lower()
        tag   = coin['symbol']
        price = round(coin['quote']['ZAR']['price'],2)
        marketcap = round(coin['quote']['ZAR']['market_cap'])
        change1h  = round(coin['quote']['ZAR']['percent_change_1h'],2)
        change24h = round(coin['quote']['ZAR']['percent_change_24h'],2)
        change7d  = round(coin['quote']['ZAR']['percent_change_7d'],2)
        change30d  = 0
        change60d  = 0
        change90d  = 0
        if (coin['quote']['ZAR']['percent_change_30d']) != None:
          change30d  = round((coin['quote']['ZAR']['percent_change_30d']),2)
        if (coin['quote']['ZAR']['percent_change_60d']) != None:
          change60d  = round((coin['quote']['ZAR']['percent_change_60d']),2)
        if (coin['quote']['ZAR']['percent_change_90d']) != None:
          change90d  = round((coin['quote']['ZAR']['percent_change_90d']),2)

        id = coin['id']
        num_market_pairs = coin['num_market_pairs']
        date_added = coin['date_added']
        circulating_supply = coin['circulating_supply']
        max_supply = coin['max_supply']
        total_supply = coin['total_supply']
        volume_24h = round(coin['quote']['ZAR']['volume_24h'])
        roi = 0
        star = ' '

        #Add spesific coins to seprate list
        if tag in wallet:
            star = '*'
        if no == 1:
          bitcoin_marketcap = marketcap
        marketcap = round(marketcap/bitcoin_marketcap, 3)
        volume_24h = round(volume_24h/bitcoin_marketcap, 3)
        
        item = CoinData(id, no, star, name, tag, price, 
        change1h, change24h, change7d, change30d, change60d, change90d, 
        roi, marketcap, num_market_pairs, date_added, circulating_supply, max_supply, total_supply, volume_24h)
        data.append(item)

        

      return data
        
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)

  def show(self, data):
          #SORTED DATA ACCORDING TO...
          hourly = sorted(data, key=operator.attrgetter('change1h'))
          daily = sorted(data, key=operator.attrgetter('change24h'))
          weekly = sorted(data, key=operator.attrgetter('change7d'))
          monthly = sorted(data, key=operator.attrgetter('change30d'))
          sixty = sorted(data, key=operator.attrgetter('change60d'))
          ninety = sorted(data, key=operator.attrgetter('change90d'))
          # persentage_change = [hourly, daily, weekly, monthly, sixty, ninety] future changes

          watchlist = CryptoData.getWatchlist(self, data)
          worst = CryptoData.getWorstPerforming(self, weekly, 30)

          DisplayData.displayData(DisplayData, hourly, daily, weekly, monthly, sixty, ninety)
          DisplayData.displayWatchlist(DisplayData, watchlist)
          DisplayData.displayWorstPerforming(DisplayData, worst)
  
  def filter(self, data, category):
    return(sorted(data, key=operator.attrgetter(category)))
      
  def findCoin(self, data, name):
      for coin in data:
          if coin.name == name:
              return coin

  def getWatchlist(self, data):
      watchlist = []
      for coin in data:
          if(coin.star == '*'):
              watchlist.append(coin)
      watchlist = CryptoData.filter(self, watchlist, 'change7d')
      watchlist.reverse()
      return watchlist

  def getWorstPerforming(self, data, n):
      worst = []
      for coin in data:
          if(coin.no <= n):
              if(coin.change7d < 0):
                  worst.append(coin)
      return worst
    
  def writeFile(self, data):
    watchlist = CryptoData.getWatchlist(CryptoData, data)

    path = 'C:\\Users\\waltd\\coding\\python\\marketcap\\watchlist_file.txt'
    message = ''

    for coin in watchlist:
      name = coin.name
      price = coin.price
      if price > 100:
        price = round(price)
      change = coin.change7d
      message += str(name) + " : R " + str(price) + " | " + str(change)+"%\n"

    with open(path, mode='w') as watchlist_file:
        watchlist_file.write(message)

       