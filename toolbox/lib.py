#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for toolbox Project
"""

from os.path import split
import pandas as pd
import datetime
import requests
import time

pd.set_option('display.width', 200)

def send_sms(*args, **kwargs):

    if kwargs:
        #print("Keyword arguments:")
        #for k, v in kwargs.items():
            #print(f' => {k}: {v}')
        number = str(kwargs['number'])
        if number[0] != "+":
            number = "+"+number
        message = str(kwargs['message'])
        path = f"?number={number}&message={message}"

        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"

        req = requests.get(BASE_URI+path).json()
        print("\nSending the SMS...\n")
        #print(req)
        return req

    else:
        print("##############################################")
        print("############# Fed Up SMS Sender ##############")
        print("##############################################")
        print("Please provide your phone number : ?")
        number = str(input())
        if number[0] != "+":
            number = "+"+number
        print("Please provide your message : ?")
        message = str(input())



        path = f"?number={number}&message={message}"
        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"
        req = requests.get(BASE_URI+path).json()
        print("\nSending the SMS...\n")
        #print(req)
        return req

def send_newsletter(*args, **kwargs):

    print("##############################################")
    print("############# Fed Up Newsletter ##############")
    print("##############################################")
    phone = pd.read_csv("data/phone_number.txt")

    phone_book = phone.to_dict()
    for person, number in phone_book.items():

        message = f"""Dear {person}, thanks for subscribing in Fed Up! Our platform will be live very soon. Stay tuned !"""
        path = f"?number={number}&message={message}"

        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"

        #req = requests.get(BASE_URI+path).json()
        req = ""
        print(f"Sending SMS to {person}...")
        time.sleep(0.2)

    print("Newsletter sent to subscribers !")
    return req


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import toolbox

