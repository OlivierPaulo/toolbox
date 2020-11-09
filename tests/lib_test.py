# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolbox
import pandas as pd
# Import from our lib
import pytest
from toolbox.lib import send_sms
from toolbox.lib import send_newsletter
from toolbox.lib import get_input
from unittest.mock import patch


# @patch('n', return_value='n')
# def test_send_sms():
#     assert send_sms() != None

# @patch('n', return_value='n')
# def test_send_newsletter():
#     assert send_newsletter() != None
