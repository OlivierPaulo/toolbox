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
#from unittest.mock import patch



pd.set_option('display.width', 200)

def get_input():
    return input()


def send_sms(*args, **kwargs):

    BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"

    if kwargs:
        #print("Keyword arguments:")
        for person, number in kwargs.items():
            #print(f' => {k}: {v}')

            message = f"""Dear {str(person).capitalize()}, thanks for subscribing in Fed Up! Our platform will be live very soon. Stay tuned !"""
            path = f"?number={number}&message={message}"

            req = requests.get(BASE_URI+path).json()
            print(f"\nSending SMS to {str(person).capitalize()}...\n")
        #print(req)
        return req

    else:
        print("##############################################")
        print("############# Fed Up SMS Sender ##############")
        print("##############################################")
        print("Please provide your phone number : ?")
        number = str(input())

        print("Please provide your message : ?")
        message = str(input())



        path = f"?number={number}&message={message}"
        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"


        print(f"Are you sure you want to send the newsletter to subscribers ? (y/n)")

        confirmation = str(input()).lower()

        if confirmation == "y":
            req = requests.get(BASE_URI+path).json()
            print("\nSending the SMS...\n")
            #print(req)
            return req
        else:
            req = "Not send"
        return req






def send_newsletter(*args, **kwargs):

    print("##############################################")
    print("############# Fed Up Newsletter ##############")
    print("##############################################")
    phone = pd.read_csv("./toolbox/data/phone_number.txt")
    print(phone)
    phone_book = phone.to_dict()
    # phone_book = {
    #     "Thierry":"+33652546065"
    # }
    #print(f"{phone_book}")
    print(f"Are you sure you want to send the newsletter to subscribers ? (y/n)")

    confirmation = str(input()).lower()

    if confirmation == "y":

        for person, number in phone_book.items():

            message = f"""Dear {person}, thanks for subscribing in Fed Up! Our platform will be live very soon. Stay tuned !"""
            path = f"?number={number}&message={message}"

            BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"

            req = requests.get(BASE_URI+path).json()

            print(f"Sending SMS to {person}...")
            time.sleep(0.2)

    if confirmation == "y":
        print("Newsletter sent to subscribers !")

    else:
        req = "Not send"
    return req


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import toolbox

