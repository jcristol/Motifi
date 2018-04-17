from threading import Thread
from queue import Queue
from Robinhood import Robinhood
from Robinhood import exceptions as RH_exception

class RobinhoodFetcher():

  def __init__(self, trader: Robinhood):
    self.rb = trader

  def getInstruments(self, targets: list) -> list:
    todo, results = Queue(len(targets)), []

    def getInstrument() -> dict:
      item = todo.get()
      try:
        result = self.rb.quote_data(item['symbol'])
        result['weight'] = item['weight']
        result['name'] = item['name']
        results.append(result)
      except:
        print("Missing Ticker {}".format(item['symbol']))
      finally:
        todo.task_done()

    for item in targets:
      t = Thread(target=getInstrument)
      t.daemon = True
      t.start()
      todo.put(item)
    todo.join()
    return results