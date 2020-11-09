# -*- coding: UTF-8 -*-

# Import from standard library
import os
import toolbox
import pandas as pd
# Import from our lib
import pytest
from toolbox.lib import send_sms
from toolbox.lib import send_newsletter

def test_send_sms():
    assert send_sms({"person":"Olivier", "number":"+33627644637"}) != None

def send_sms():
    assert send_sms({"person":"Olivier", "number":"+33627644637"}) != None
