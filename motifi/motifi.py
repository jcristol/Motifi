import motifi.spreadsheet as sheets
from motifi.trade import PaperTrader 
from motifi.api import RobinhoodFetcher
from Robinhood import Robinhood

def run(total_cash: float, spreadsheets: list, trade_type=None):
  paper = PaperTrader(total_cash, spreadsheets)
  paper.prePrint()
  paper.runTrader()
  paper.postPrint()
