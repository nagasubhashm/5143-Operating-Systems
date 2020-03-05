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

    if not period is False:
        # get historical market data
        #hist = data.history(period="max")
        history = data.history(period=period)

        #print(hist)
        hist_path = os.path.join(path,f"{symbol}_{period}.csv")
        history.to_csv(hist_path)
    


def loadStockSymbols(path):
    symbols = []
    fp = open(path,'r')
    data = fp.readlines()
    for d in data:
        d = d.split(",")
        symb = d[0]
        if symb.isalnum() and not symb in symbols:
            symbols.append(symb)
    return symbols
    

def logg(message):
    f = open

if __name__=='__main__':
    
    symbol_path = "./data/symbol_data/all.csv"
    ticker_path = "./data/ticker_data/"

    if os.path.isdir(os.path.dirname(__file__)):
        os.chdir(os.path.dirname(__file__))

    if not os.path.isfile(symbol_path):
        logging.critical(f"File doesn't exist: {symbol_path}")

    if not os.path.isdir(ticker_path):
        logging.warning(f"Directory doesn't exist: {ticker_path} creatin it now ...")
        os.mkdir(ticker_path)

    symbols = loadStockSymbols(symbol_path)

    #shuffle(symbols)

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
