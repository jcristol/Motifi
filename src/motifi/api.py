from threading import Thread
from queue import Queue
from rhwrapper.Robinhood import Robinhood

class RobinhoodFetcher():

  def __init__(self, trader: Robinhood):
    self.rb = trader

  def getInstruments(self, targets: list) -> list:
    todo, results = Queue(len(targets)), []

    def getInstrument() -> dict:
      item = todo.get()
      result = self.rb.quote_data(item['symbol'])
      result['weight'] = item['weight']
      results.append(result)
      todo.task_done()

    for item in targets:
      t = Thread(target=getInstrument)
      t.daemon = True
      t.start()
      todo.put(item)
    todo.join()
    return results