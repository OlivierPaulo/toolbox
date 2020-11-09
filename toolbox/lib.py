# -*- coding: UTF-8 -*-
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

def send_newsletter():
    phone_book = {
        "Andrea":"+818054675605",
        "Antonia":"+491752076835",
        "August":"+491745121996",
        "Ben":"+447763768806",
        "Charlotte":"+32475700025",
        "Helder":"+447729286273",
        "Jessica":"+33679132104",
        "Joao":"+351912865211",
        "José":"+351961416759",
        "Leonor":"+351914366147",
        "Liam":"+351911829951",
        "Lucia":"+34607542999",
        "Lukas":"+41795473233",
        "Luna":"+33668207126",
        "Matthieu":"+33768354829",
        "Mia":"+447467946899",
        "Nicolo":"+393404169022",
        "Nuno":"+351916689739",
        "Pedro":"+351919658109",
        "Phillip":"+491748312746",
        "Ricardo":"+351938166489",
        "Shannon":"+351911089530"
    }
    print("##############################################")
    print("############# Fed Up Newsletter ##############")
    print("##############################################")

    for person, number in phone_book.items():

        message = f"""Dear {person}, thanks for subscribing in Fed Up! Our platform will be live very soon. Stay tuned !"""
        path = f"?number={number}&message={message}"

        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic"

        req = requests.get(BASE_URI+path).json()

        print(f"Sending SMS to {person}...")
        time.sleep(0.5)

    return req


if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import toolbox

