# Created By: Mei Li
# Date Created: 9-Mar-2021
# Last Updated: 23-Mar-2021
'''
The purpose of this program is to simulate market data for a MongoDB database. 

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

# Drop previous database
dbToDrop = 'sim_db'
client.drop_database(dbToDrop)

# Access db using attribute style access on MongoClient instances
# Make sure db name can be used in attribute style
db = client.sim_db

# Create a capped collection
collection_parameters = {"capped" : True, "size" : 2147483648}
collection = db.create_collection("stocks", **collection_parameters)
posts = [
    {"symbol": "AAPL",
    "price": "2",
    "bid": "1",
    "ask": "1",
    "accvol": "1",
    "open": "1",
    "prev": "1",
    "change": "1",
    "changepct": "1",
    "type": "1",
    "msg":"1"},
    {"symbol": "GME",
    "price": "2",
    "bid": "2",
    "ask": "2",
    "accvol": "2",
    "open": "2",
    "prev": "2",
    "change": "2",
    "changepct": "2",
    "type": "2",
    "msg":"2"},
    {"symbol": "BB",
    "price": "3",
    "bid": "3",
    "ask": "3",
    "accvol": "3",
    "open": "3",
    "prev": "3",
    "change": "3",
    "changepct": "3",
    "type": "3",
    "msg":"3"},
    ]
# Single post 
'''
post = {"symbol": "AAPL",
    "price": "2",
    "bid": "1",
    "ask": "1",
    "accvol": "1",
    "open": "1",
    "prev": "1",
    "change": "1",
    "changepct": "1",
    "type": "1",
    "msg":"1"}
'''

# Insert into collection
collection.insert_many(posts)

# Prints collection status
# pprint(collection)

# Create a list to store stocks
total = 10
stocks = list()

for i in range(total):
    symbol = ''.join(random.choices(string.ascii_uppercase, k=3))
    stocks.append(symbol)
    #print(symbol, " ", stocks[i])

# To stop, exit in the cmd prompt
while(True):
    # Randomly pick an index for the symbol
    randInd = randrange(total)
    symbol = stocks[randInd]
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
