import motifi.spreadsheet as sheets
from motifi.api import RobinhoodFetcher
from Robinhood import Robinhood

def run(total_cash: float, spreadsheets: list):
  m = Motifi()
  for spreadsheet in spreadsheets:
    run_sheet(total_cash / len(spreadsheets), spreadsheet, m)

def run_sheet(cash: float, spreadsheet: str, motif):
  targets: list
  purchases: list
  targets = sheets.read_excel(spreadsheet)
  print("Paper Trading the motif {}".format(spreadsheet))
  purchases, gross_total = motif.paperTrade(cash, targets)
  for p in purchases:
    print("Paper Trade {} shares of {} : {} at $ {}".format(p['quantity'], p['name'], p['symbol'], p['bid_price']))
  print("Grand Total $ {}".format(gross_total))

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
