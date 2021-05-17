#!/usr/bin/env python3

from flask import Flask, jsonify, request
from json import dumps
from flask_restful import Resource, Api
from urllib.request import urlopen
from urllib.error import HTTPError
import json
import os
import requests
import sys
import yaml


app = Flask(__name__)
stockapi = Api(app)


def get_jsonparsed_data(url):
    """
    Receive the content of ``url``,
    parse it as JSON and return the object.

    Parameters
    ----------
    url : str

    Returns
    -------
    dict
    """
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


class APIFunctions(object):

    def check_load_key():
        '''
        Check for file named .key and load it.
        Contains API key for  https://financialmodelingprep.com/developer/docs/
        Load into blank list and return usable str type key
        '''
        key_file = '.key'
        if not os.path.exists(key_file):
            return 'Error! API Key for FMP is not saved as .key in repo'
        else:
            api_key_list = []
            with open(key_file) as file:
                for line in file:
                    api_key_list.append(line)

                    key_string = ''.join(api_key_list)
                    return_string = key_string.strip('\n')
                    return return_string


    def __init__(self):
        self.API_KEY = APIFunctions.check_load_key()

    def get_ticker(self, ticker):
        '''
        Show basic ticker quote and info
        '''
        for t in ticker:
            url = f"https://financialmodelingprep.com/api/v3/quote-short/{t}?apikey={self.API_KEY}"
            try:
                data = get_jsonparsed_data(url)
            except HTTPError as e:
                print(e)
        return data

    def get_profile(self, ticker):
        '''
        Show detailed company information
        '''
        url = f"https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={self.API_KEY}"
        try:
            data = get_jsonparsed_data(url)
        except HTTPError as e:
            print(e)
        return data

    def get_executives(self, ticker):
        '''
        Show key company executives
        '''
        url = f"https://financialmodelingprep.com/api/v3/key-executives/{ticker}?apikey={self.API_KEY}"
        try:
            data = get_jsonparsed_data(url)
        except HTTPError as e:
            print(e)
        return data

    def get_news(self, ticker):
        '''
        Show ticker news.TODO: Add support for multiple tickers
        '''
        url = f"https://financialmodelingprep.com/api/v3/stock_news?tickers={ticker}&limit=50&apikey={self.API_KEY}"
        try:
            data = get_jsonparsed_data(url)
        except HTTPError as e:
            print(e)
        return data


api_functions = APIFunctions()


@app.route("/quote/<x>")
def get_quote(x):
    quote = api_functions.get_ticker(x)
    return jsonify(quote)


@app.route("/profile/<y>")
def get_profile(y):
    quote = api_functions.get_profile(y)
    return jsonify(quote)


@app.route("/executives/<z>")
def get_executives(z):
    quote = api_functions.get_executives(z)
    return jsonify(quote)


@app.route("/news/<i>")
def get_news(i):
    quote = api_functions.get_news(i)
    return jsonify(quote)


if __name__ == '__main__':
    app.run(debug=True)
