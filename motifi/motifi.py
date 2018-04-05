import motifi.spreadsheet as sheets
from motifi.api import RobinhoodFetcher
from rhwrapper.Robinhood import Robinhood

def run(cash: float, spreadsheets: list):
  for spreadsheet in spreadsheets:
    divided_cash = cash / len(spreadsheets)
    targets: list = sheets.read_excel(spreadsheet)
    m = Motifi()
    print("Paper Trading the motif {}".format(spreadsheet))
    purchases, gross_purchases = m.paperTrade(divided_cash, targets)
    purchases: list
    gross_purchases: float
    for p in purchases:
      print("Paper Trade {} shares of {} : {} at $ {}".format(p['quantity'], p['name'], p['symbol'], p['bid_price']))
    print("Grand Total $ {}".format(gross_purchases))

class Motifi():

  def __init__(self):
    self.rb = Robinhood()

  def paperTrade(self, cash: float, targets: list) -> tuple:
    """
    returns list of purchase dictionaries
    """
    def purchase(instrument: dict):
      bid_price, symbol, name, weight = float(instrument['bid_price']), instrument['symbol'], instrument['name'], float(instrument['weight'])
      cash_avaliable = weight * cash
      buys = cash_avaliable // bid_price
      buys = max(0, buys)
      return {
        'symbol' : symbol,
        'quantity' : buys,
        'name' : name,
        'bid_price' : bid_price
      }
    api = RobinhoodFetcher(self.rb)
    instruments = api.getInstruments(targets)
    purchases = [ purchase(i) for i in instruments ]
    gross_purchases: float = sum(map(lambda p: p['quantity'] * p['bid_price'], purchases))
    gross_purchases = round(gross_purchases, 2)
    return (purchases, gross_purchases)
