'''
The purpose of this program is to simulate market data for a MongoDB database. 

'''

import pymongo
import datetime
import random
import string 
import time
from random import randrange
# pprint library is used to make output look pretty
#from pprint import pprint

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

# Prints collection status
# pprint(collection)

# Create a list to store stock symbols
stocks = list()
stocks = ['AAPL','TSLA','BB','GME','NIO','TME','FEDU','VIPS','EDU','AMC','SPY','BAC','PLTR','XLF','T','GE','F','EEM','NOK','TAL']

# To stop, exit in the cmd prompt
while(True):
    # Randomly pick an index for the symbol and output in cmd prompt
    randInd = randrange(len(stocks))
    symbol = stocks[randInd]
    print(symbol)

    # Randomly generate new fields for the symbol
    price = str(randrange(100))
    bid = str(randrange(100))
    ask = str(randrange(100))

    post = {
        "symbol": symbol,
        "price": price,
        "bid": bid,
        "ask": ask
    }
    
    # Insert new post into collection
    collection.insert_one(post)

    sleepDuration = randrange(2)
    time.sleep(sleepDuration)
