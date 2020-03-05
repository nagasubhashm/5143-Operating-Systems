#!/usr/local/bin/python3

import os,sys
import pandas as pd
import yfinance as yf
import yahoofinancials
import yfinance as yf
import json
import logging
from  random import shuffle

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def stockLookup(symbol,period,path="./ticker_data/"):
    """
    symbol: stock symbol
    period: e.g. 1y (or 1 year) 5y (or 5 years) 1ds (or 1 day) 
                see here: https://aroussi.com/post/python-yahoo-finance
    path: where to write data
    """
    data = yf.Ticker(symbol)

    try:
        null = data.institutional_holders
    except:
        logging.critical(f"Exception getting:  {symbol} ... ")
        return
    
    # get stock info    
    info = json.dumps(data.info,indent=4)
    info_path = os.path.join(path,f"{symbol}_data.csv")

    with open(info_path,"w") as f:
        f.write(info)

    # if we pass in a period of time to read
    if not period is False:
        # get historical market data
        history = data.history(period=period)

        hist_path = os.path.join(path,f"{symbol}_{period}.csv")
        history.to_csv(hist_path)
    


def loadStockSymbols(path):
    """ read stock symbols from csv into list
    """
    symbols = []
    fp = open(path,'r')
    data = fp.readlines()
    for d in data:
        d = d.split(",")
        symb = d[0]
        if symb.isalnum() and not symb in symbols:
            symbols.append(symb)
    return symbols


if __name__=='__main__':
    
    # set path for getting symbols and storing data.
    symbol_path = "./data/symbol_data/all.csv"
    ticker_path = "./data/ticker_data/"

    # make sure I'm in the directory of the file running
    # (vscode loves to make the cwd NOT where you are)
    if os.path.isdir(os.path.dirname(__file__)):
        os.chdir(os.path.dirname(__file__))

    # log error if stock symbol files not where they should be 
    if not os.path.isfile(symbol_path):
        logging.critical(f"File doesn't exist: {symbol_path}")

    # make sure directory exists
    if not os.path.isdir(ticker_path):
        logging.warning(f"Directory doesn't exist: {ticker_path} creatin it now ...")
        os.mkdir(ticker_path)

    # load up stock symbols into list
    symbols = loadStockSymbols(symbol_path)

    # randomize them (since I started running 4 instances :) )
    shuffle(symbols)

    # this loop gets the "info"
    for symbol in symbols:
        if(os.path.isfile(os.path.join(ticker_path,symbol+'_data.csv'))):
            continue
        try:
            stockLookup(symbol,False,ticker_path)
            
        except AssertionError as error:
            print(error)
        else:
            try:
                fp = open('progress.dat','a')
                fp.write(f"Last stock processed: {symbol} \n")
            except FileNotFoundError as fnf_error:
                print(fnf_error)
        finally:
            logging.critical(f"Chocked on stock: {symbol} getting info not history ...")
        print(symbol)

    # this loop gets historical data 
    for symbol in symbols:
        if(os.path.isfile(os.path.join(ticker_path,symbol+'_max.csv'))):
            continue
        try:
            stockLookup(symbol,"max",ticker_path)
        except AssertionError as error:
            print(error)
        else:
            try:
                fp = open('progress.dat','a')
                fp.write(f"Last stock processed: {symbol} \n")
            except FileNotFoundError as fnf_error:
                print(fnf_error)
        finally:
            logging.critical(f"Chocked on stock: {symbol} getting history data ...")
        print(symbol)
