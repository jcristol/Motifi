# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re
from motifi.motifi import run
from motifi.motifi import Motifi

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"

targets = [{'name': 'Salesforce.com Inc', 'weight': 0.206, 'symbol': 'CRM'}, {'name': 'The Ultimate Software Group Inc.', 'weight': 0.1238, 'symbol': 'ULTI'}, {'name': 'ServiceNow Inc.', 'weight': 0.1073, 'symbol': 'NOW'}, {'name': 'Workday Inc.', 'weight': 0.0865, 'symbol': 'WDAY'}, {'name': 'Callidus Software Inc.', 'weight': 0.0434, 'symbol': 'CALD'}, {'name': 'Cornerstone OnDemand Inc.', 'weight': 0.0418, 'symbol': 'CSOD'}, {'name': 'Shopify Inc. Class A Subordinate', 'weight': 0.0409, 'symbol': 'SHOP'}, {'name': 'New Relic Inc.', 'weight': 0.0398, 'symbol': 'NEWR'}, {'name': 'SPS Commerce Inc', 'weight': 0.0232, 'symbol': 'SPSC'}, {'name': 'RealPage Inc.', 'weight': 0.0569, 'symbol': 'RP'}, {'name': 'Athenahealth Inc.', 'weight': 0.0426, 'symbol': 'ATHN'}, {'name': 'Medidata Solutions Inc.', 'weight': 0.0321, 'symbol': 'MDSO'}, {'name': 'HealthStream Inc.', 'weight': 0.0164, 'symbol': 'HSTM'}, {'name': 'Q2 Holdings Inc.', 'weight': 0.0091, 'symbol': 'QTWO'}, {'name': 'Yext Inc.', 'weight': 0.025, 'symbol': 'YEXT'}, {'name': 'LivePerson Inc.', 'weight': 0.019, 'symbol': 'LPSN'}, {'name': 'HubSpot Inc.', 'weight': 0.013, 'symbol': 'HUBS'}, {'name': 'LogMeIn Inc.', 'weight': 0.0405, 'symbol': 'LOGM'}, {'name': 'Twilio Inc. Class A', 'weight': 0.0146, 'symbol': 'TWLO'}, {'name': 'Qualys Inc.', 'weight': 0.0182, 'symbol': 'QLYS'}] 
cash = 20000

def test_run(capsys):
  """
  checks each line of output aganist a regular expression
  """
  run(cash, ['./tests/testsheet1.xlsx', './tests/testsheet2.xlsx', './tests/testsheet3.xlsx'])
  out, err = capsys.readouterr()
  for line in out.splitlines():
    a = re.match("\.*Paper\.*",line)
    b = re.match("\.*Grand\.*",line)
    assert a or b 

def test_paper_trading():
  m = Motifi()
  purchases, gross_purchases = m.paperTrade(cash, targets)
  purchases: list
  gross_purchases: float
  for p in purchases:
    assert 'symbol' in p
    assert 'quantity' in p
    assert 'name' in p
    assert 'bid_price' in p
    assert isinstance(p['symbol'], str)
    assert isinstance(p['quantity'], float)
    assert isinstance(p['name'], str)
    assert isinstance(p['bid_price'], float)

  assert gross_purchases >= 0
  assert gross_purchases <= cash