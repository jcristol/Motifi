import motifi.spreadsheet as sheets
from rhwrapper.Robinhood import Robinhood

def run(cash: float, spreadsheet: str):
  targets: list = sheets.read_excel(spreadsheet)
  m = Motifi()



class Motifi():

  def __init__(self):
    self.rb = Robinhood()

  def paperTrade(self, cash: float, targets: list) -> list:
    # get information from the api 
    # return the information
    pass
