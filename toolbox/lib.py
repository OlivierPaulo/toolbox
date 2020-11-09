# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for toolbox Project
"""

from os.path import split
import pandas as pd
import datetime
import requests

pd.set_option('display.width', 200)


def clean_data(data):
    """ clean data
    """
    # Remove columns starts with vote
    cols = [x for x in data.columns if x.find('vote') >= 0]
    data.drop(cols, axis=1, inplace=True)
    # Remove special characteres from columns
    data.loc[:, 'civility'] = data['civility'].replace('\.', '', regex=True)
    # Calculate Age from day of birth
    actual_year = datetime.datetime.now().year
    data.loc[:, 'Year_Month'] = pd.to_datetime(data.birthdate)
    data.loc[:, 'Age'] = actual_year - data['Year_Month'].dt.year
    # Uppercase variable to avoid duplicates
    data.loc[:, 'city'] = data['city'].str.upper()
    # Take 2 first digits, 2700 -> 02700 so first two are region
    data.loc[:, 'postal_code'] = data.postal_code.str.zfill(5).str[0:2]
    # Remove columns with more than 50% of nans
    cnans = data.shape[0] / 2
    data = data.dropna(thresh=cnans, axis=1)
    # Remove rows with more than 50% of nans
    rnans = data.shape[1] / 2
    data = data.dropna(thresh=rnans, axis=0)
    # Discretize based on quantiles
    data.loc[:, 'duration'] = pd.qcut(data['surveyduration'], 10)
    # Discretize based on values
    data.loc[:, 'Age'] = pd.cut(data['Age'], 10)
    # Rename columns
    data.rename(columns={'q1': 'Frequency'}, inplace=True)
    # Transform type of columns
    data.loc[:, 'Frequency'] = data['Frequency'].astype(int)
    # Rename values in rows
    drows = {1: 'Manytimes', 2: 'Onetimebyday', 3: '5/6timesforweek',
             4: '4timesforweek', 5: '1/3timesforweek', 6: '1timeformonth',
             7: '1/trimestre', 8: 'Less', 9: 'Never'}
    data.loc[:, 'Frequency'] = data['Frequency'].map(drows)
    return data


def send_sms(*args, **kwargs):

    if kwargs:
        #print("Keyword arguments:")
        #for k, v in kwargs.items():
            #print(f' => {k}: {v}')
        number = kwargs['number']
        message = kwargs['message']
        path = f"?number={number}&message={message}"
        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic{path}"
        req = requests.get(BASE_URI+path).json()
        return req
    else:
        print("Please provide your phone number : ?\n")
        number = str(input())
        print("Please provide your message : ?\n")
        message = str(input())

        path = f"?number={number}&message={message}"
        BASE_URI = f"https://hook.integromat.com/kg9mm79dgr5pp7m2d5w2nwch18kwrqic{path}"
        req = requests.get(BASE_URI+path).json()
        return req


def daily_forecast(woeid, year, month, day):
    path = f"/api/location/{woeid}/{year}/{month}/{day}"
    response = requests.get(BASE_URI+path).json()
    #print(response)
    return response

if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import toolbox
    folder_source, _ = split(toolbox.__file__)
    df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    clean_data = clean_data(df)
    print(' dataframe cleaned')
