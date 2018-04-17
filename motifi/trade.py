from Robinhood import Robinhood
from motifi.api import RobinhoodFetcher
import motifi.spreadsheet as sheets

class Trade():

  def __init__(self, total_cash: float, spreadsheets: list):
    self.total_cash = total_cash
    self.spreadsheets = spreadsheets
    self.rb = Robinhood()
    self.results = []

  def runTrader(self):
    raise NotImplementedError("runTrader not implemented for trader {}".format(self))

  def prePrint(self):
    [print("Paper Trading the motif {}".format(spreadsheet)) for spreadsheet in self.spreadsheets]
    print("Spending {} dollars".format(self.total_cash))

  def postPrint(self):
    """
    must call after running the trader
    """
    for res in self.results:
      trades, total_spent = res
      for t in trades:
        print("Paper Trade {} shares of {} : {} at $ {}".format(t['quantity'], t['name'], t['symbol'], t['bid_price']))
      print("Total spent on portfolio $ {}".format(total_spent))


class PaperTrader(Trade):
  
  def runTrader(self):
    cash_per_sheet = self.total_cash / len(self.spreadsheets)
    for sheet in self.spreadsheets:
      targets = sheets.read_excel(sheet)
      self.results += [self.paperTrade(targets, cash_per_sheet)]

  def paperTrade(self, targets: list, cash: float):

    def task(instrument: dict):
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
    trades = [ task(i) for i in instruments ]
    spent: float = sum(map(lambda t: t['quantity'] * t['bid_price'], trades))
    spent = round(spent, 2)
    return (trades, spent)

