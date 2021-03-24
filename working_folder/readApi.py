"""
Created on March 2021 by Damaso Sanchez Arenas.

File where we read the information from the api and generate the differents .csv
"""

import pandas as pd
import requests as rq
import json
import logging 
import datetime
from constants import *
from commonsFunctions import *
logging.basicConfig(
    filename=FILE_LOG_PATH,
    encoding='utf-8', 
    level=logging.INFO
)

'''
In this method we read from the api and we get the woeid of the city
'''
def obtain_woeid(city):
    request = rq.get(URI + f'/api/location/search/?query={city}', HEADER)
    woeid = json.loads(request.content.decode("utf-8"))[0]["woeid"]
    logging.info(WOEID_STR + city + ' : ' + str(woeid))

    return woeid

'''
In this method we can read the consolidated_weather of each city from the api
'''
def obtain_consolidated_weather(woeid):
    request = rq.get(URI + f'/api/location/{woeid}', HEADER)
    consolidated_weather = json.loads(request.content.decode("utf-8"))["consolidated_weather"]

    return consolidated_weather

'''
With this method we will read the corresponding information from the api and generate
a csv for each of the cities
'''
def read_from_api():
    #Loggers
    logs_handlers()

    #The selected cities have been London Madrid and Boston. (You can change them in constants.py)
    #The csv will be saved in the place where you are executing this script (readApi.csv)
    
    for city in CITIES:
        path = obtain_path()

        #obtain the info
        woeid = obtain_woeid(city)
        json_consolidated_weather = obtain_consolidated_weather(woeid) 
        
        #Convert the info
        df_consolidated_weather = json_to_DF(json_consolidated_weather)        
        DF_to_CSV(df_consolidated_weather,city)

    logging.info(CVS_GENERATED_STR + path + END_LINE)

if __name__ == '__main__':
    read_from_api()