# Created By: Mei Li
# Date Created: 14-Mar-2021
# Last Updated: 14-Mar-2021
'''
The purpose of this program is to simulate market data for an exisitng database and collection in MongoDB.

'''

import pymongo
import datetime
# pprint library is used to make output look pretty
from pprint import pprint

import random
import string 
import time
from random import randrange

# Create a MongoClient to the running mongo instance
from pymongo import MongoClient
# Specify the host and port
client = MongoClient('localhost', 27017)
#client = MongoClient('mongodb://localhost:27017/')

# Access db using attribute style access on MongoClient instances
# Make sure db name can be used in attribute style
# Access collection
db = client.IceSource_db
collection = db.icestockl1

# Create a list to store stocks
total = 4
stocks = ["IBM", "BAC", "BABA", "F", "C"]

# To stop, exit in the cmd prompt
while(True):
    # Randomly pick an index for the symbol
    num = random.randint(0,total)
    symbol = stocks[num]
    print(symbol)

    # Randomly generate new fields for the symbol
    price = str(randrange(100))
    bid = str(randrange(100))
    ask = str(randrange(100))
    accvol = str(randrange(100))
    openStr = str(randrange(100))
    prev = str(randrange(100))
    change = str(randrange(100))
    changepct = str(randrange(100))
    typeStr = str(randrange(100))
    msg = str(randrange(100))

    post = {
        "symbol": symbol,
        "price": price,
        "bid": bid,
        "ask": ask,
        "accvol": accvol,
        "open": openStr,
        "prev": prev,
        "change": change,
        "changepct": changepct,
        "type": typeStr,
        "msg":msg
    }
    
    # Insert new post into collection
    collection.insert_one(post)

    sleepDuration = randrange(5)
    time.sleep(sleepDuration)
