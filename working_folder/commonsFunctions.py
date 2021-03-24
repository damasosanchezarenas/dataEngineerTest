"""
Created on March 2021 by Damaso Sanchez Arenas.

File where all the common functions of the project are.
"""

import sys
import os
import pandas as pd
import requests as rq
import json
import logging 
import datetime
import pymongo
import dns
from constants import *
import configparser
import connection
logging.basicConfig(
    filename=FILE_LOG_PATH,
    encoding='utf-8',
    level=logging.INFO
)

'''
Thanks to this method we can show the logs on screen and by file
'''
def logs_handlers():
    #If the root logger already has handlers, they are removed before adding the new ones.
    #This is important so that the logs do not start to duplicate.
    if logging.getLogger('').hasHandlers():
        logging.getLogger('').handlers.clear()

    #Handler with output to file
    file_handler = logging.FileHandler(FILE_LOG_PATH)
    logging.getLogger('').addHandler(file_handler)

    #Handler with output to console
    console_handler = logging.StreamHandler()
    logging.getLogger('').addHandler(console_handler)

'''
This method is to obtain the path where save the .csv files
'''
def obtain_path():
    return os.getcwd()

'''
This method is to obtain an id (timestamp), to be able to save as many .csv we want without being overwritten
'''
def obtain_timestamp():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    return current_time.timestamp()

'''
This method is used to convert from json to DF
'''
def json_to_DF(json):
    df = pd.DataFrame(json)
    return df

'''
This method is used to convert from DF to CSV
'''
def DF_to_CSV(df, city):
    return df.to_csv(f'weather_{city}.csv', index=False)

'''
This method is used to convert from DF to CSV
'''
def DF_to_json(df, orient):
    return  df.to_json(orient = orient)

'''
Method to get the user from the file "config.init"
'''
def get_user_ddbb():
    config = configparser.ConfigParser()
    config.read(FILE_CONFIG_PATH)
    return config['MONGODB']['user']

'''
Method to get the pass from the file "config.init"
'''
def get_pass_ddbb():
    config = configparser.ConfigParser()
    config.read(FILE_CONFIG_PATH)
    return config['MONGODB']['pass']

'''
Method to get the database name from the file "config.init"
'''
def get_name_ddbb():
    config = configparser.ConfigParser()
    config.read(FILE_CONFIG_PATH)
    return config['MONGODB']['db_name']

'''
Method to connect to the mongo database
'''
def connect_db():

    try:
        #connect to BD 
        user = get_user_ddbb()
        passw = get_pass_ddbb()
        db_name = get_name_ddbb()

        client = pymongo.MongoClient(f"mongodb+srv://{user}:{passw}@cluster0.8edgo.mongodb.net/{db_name}?retryWrites=true&w=majority")
        db = client.metaWeather

    except pymongo.errors.ConnectionFailure:
        logging.Critical(CONNECTION_ERROR_STR)

    return db

'''
Method to save documents in mongodb
'''
def add_docs_mongoDB(db, collection_name, json):
    try:
        exec(f'db.{collection_name}.insert_many({json})')
    except e:
        logging.Critical(e)


'''
Method to delete documents in mongodb
'''
def remove_docs_mongoDB(db,collection_name,docs):
    try:
        exec(f'db.{collection_name}.delete_many({docs})')
    except e:
        logging.Critical(e)


'''
Method to find documents in mongodb
'''
def find_docs_mongoDB(rows,docs):
    return list(rows.find(docs, {"_id": 0})) 