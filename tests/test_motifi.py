# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import re
from motifi.motifi import run

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"


def test_run(capsys):
  """
  checks each line of output aganist a regular expression
  """
  run(200000, 'testsheet.xlsx')
  out, err = capsys.readouterr()
  for line in out.splitlines():
    a = re.match("\.*Paper\.*",line)
    b = re.match("\.*Grand\.*",line)
    assert a or b 

