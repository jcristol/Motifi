# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from motifi.trade import PaperTrader

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"

cash = 20000

def test_paperTrade():
  sheets = ['./tests/testsheet1.xlsx', './tests/testsheet2.xlsx', './tests/testsheet3.xlsx']
  p = PaperTrader(cash, sheets)
  p.prePrint()
  p.runTrader()
  p.postPrint()
  results = p.results
  assert len(results) > 0
  split_cash = cash / len(sheets)
  for res in results:
    trades, total = res
    assert total <= split_cash
    for t in trades:
      assert 'symbol' in t
      assert 'quantity' in t
      assert 'name' in t
      assert 'bid_price' in t