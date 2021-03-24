"""
Created on March 2021 by Damaso Sanchez Arenas.

File where we will save the information in a mongoDB database
"""

import pandas as pd
import json
import glob
import pymongo
import dns
import logging 
from commonsFunctions import *
from constants import *
logging.basicConfig(
    filename=FILE_LOG_PATH,
    encoding='utf-8',
    level=logging.DEBUG
)

'''
in this method we are going to write the corresponding csv in the database
'''
def write(): 

    #Loggers
    logs_handlers()

    #Obtain the diferents *.csv
    files_list = glob.glob(obtain_path()+ '/' + '*.csv')
    
    #Connect with the database
    db = connect_db()
  
    for file in files_list:
        #Transformation with the name of the .csv
        file_name_format =  file.split('\\')[-1]
        collection_name = file.split('.')[0].split('weather_')[-1]

        #Convert the .csv to DF
        df = pd.read_csv(file)

        #Convert the DF to json and load it
        json_df = json.loads(DF_to_json(df, "records"))

        #Save data in mongoDB. If that collection already exists, I delete it before saving the new one.

        docs = '{}' #'{}' because we want to delete all the collection
        remove_docs_mongoDB(db,collection_name,docs) 
        add_docs_mongoDB(db,collection_name,json_df)

        logging.info(file_name_format + ARROW_STR + SAVE_DATA_STR)

if __name__ == '__main__':
    write()