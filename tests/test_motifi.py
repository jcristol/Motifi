# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re
from motifi.motifi import run

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"

cash = 20000

def test_run(capsys):
  """
  checks each line of output aganist a regular expression
  """
  run(cash, ['./tests/testsheet1.xlsx', './tests/testsheet2.xlsx', './tests/testsheet3.xlsx'])
  out, err = capsys.readouterr()
  for line in out.splitlines():
    a = re.match("\.*Paper \.*",line)
    b = re.match("\.*Total spent\.*",line)
    c = re.match("\.*Missing Ticker\.*",line)
    d = re.match("\.*Spending\.*",line)
    assert a or b or c or d
