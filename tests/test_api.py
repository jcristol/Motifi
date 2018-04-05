#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from motifi.api import RobinhoodFetcher
from rhwrapper.Robinhood import Robinhood

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"

rb = Robinhood()
targets = [{'name': 'Salesforce.com Inc', 'weight': 0.206, 'symbol': 'CRM'}, {'name': 'The Ultimate Software Group Inc.', 'weight': 0.1238, 'symbol': 'ULTI'}, {'name': 'ServiceNow Inc.', 'weight': 0.1073, 'symbol': 'NOW'}]


def test_api():
  f = RobinhoodFetcher(rb)
  instruments = f.getInstruments(targets)
  for i in instruments:
    assert 'ask_price' in i
    assert 'ask_size' in i
    assert 'weight' in i
    assert 'symbol' in i