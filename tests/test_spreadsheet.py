# !/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from motifi.spreadsheet import read_excel

__author__ = "jcristol"
__copyright__ = "jcristol"
__license__ = "mit"

test_excel_path = "testsheet.xlsx"
exp = [{'Name': 'Salesforce.com Inc', 'Weight': 0.206, 'Symbol': 'CRM'}, {'Name': 'The Ultimate Software Group Inc.', 'Weight': 0.1238, 'Symbol': 'ULTI'}, {'Name': 'ServiceNow Inc.', 'Weight': 0.1073, 'Symbol': 'NOW'}, {'Name': 'Workday Inc.', 'Weight': 0.0865, 'Symbol': 'WDAY'}, {'Name': 'Callidus Software Inc.', 'Weight': 0.0434, 'Symbol': 'CALD'}, {'Name': 'Cornerstone OnDemand Inc.', 'Weight': 0.0418, 'Symbol': 'CSOD'}, {'Name': 'Shopify Inc. Class A Subordinate', 'Weight': 0.0409, 'Symbol': 'SHOP'}, {'Name': 'New Relic Inc.', 'Weight': 0.0398, 'Symbol': 'NEWR'}, {'Name': 'SPS Commerce Inc', 'Weight': 0.0232, 'Symbol': 'SPSC'}, {'Name': 'RealPage Inc.', 'Weight': 0.0569, 'Symbol': 'RP'}, {'Name': 'Athenahealth Inc.', 'Weight': 0.0426, 'Symbol': 'ATHN'}, {'Name': 'Medidata Solutions Inc.', 'Weight': 0.0321, 'Symbol': 'MDSO'}, {'Name': 'HealthStream Inc.', 'Weight': 0.0164, 'Symbol': 'HSTM'}, {'Name': 'Q2 Holdings Inc.', 'Weight': 0.0091, 'Symbol': 'QTWO'}, {'Name': 'Yext Inc.', 'Weight': 0.025, 'Symbol': 'YEXT'}, {'Name': 'LivePerson Inc.', 'Weight': 0.019, 'Symbol': 'LPSN'}, {'Name': 'HubSpot Inc.', 'Weight': 0.013, 'Symbol': 'HUBS'}, {'Name': 'LogMeIn Inc.', 'Weight': 0.0405, 'Symbol': 'LOGM'}, {'Name': 'Twilio Inc. Class A', 'Weight': 0.0146, 'Symbol': 'TWLO'}, {'Name': 'Qualys Inc.', 'Weight': 0.0182, 'Symbol': 'QLYS'}]

def test_read_excel():
  res = read_excel(test_excel_path)
  assert res == exp