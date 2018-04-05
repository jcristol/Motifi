import motifi.spreadsheet as sheets
from motifi.api import RobinhoodFetcher
from rhwrapper.Robinhood import Robinhood

def run(cash: float, spreadsheet: str):
  targets: list = sheets.read_excel(spreadsheet)
  m = Motifi()

class Motifi():

  def __init__(self):
    self.rb = Robinhood()

  def paperTrade(self, cash: float, targets: list) -> list:
    """
    gets the instrument data for all the targets
    """
    api = RobinhoodFetcher(self.rb)
    return api.getInstruments(targets)