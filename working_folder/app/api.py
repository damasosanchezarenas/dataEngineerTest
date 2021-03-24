"""
Created on March 2021 by Damaso Sanchez Arenas.

File with the api of the project.
"""
import requests as rq
import pymongo
import sys
import configparser
import dns
import connection
import logging
sys.path.append(r"C:\Users\jesus\cw\data-engineer-exercise\working_folder")
from commonsFunctions import *
from constants import *
from flask import Flask, request, render_template, jsonify
logging.basicConfig(
    format = '%(asctime)-5s %(name)-15s %(levelname)-8s %(message)s', 
    filename=FILE_LOG_PATH,
    encoding='utf-8', 
    level=logging.INFO
)

#Loggers
logs_handlers()

#Connect with the database
db = connect_db()

#Logs messages
logging.info(END_LINE)
logging.info(CONNECTED_STR)
logging.info(CONNECT_TO_API_STR)
logging.info(CONSOLE_TO_API_STR)
logging.info(EXIT_STR)


#Create the app Flask
app = Flask(__name__) 

@app.route('/api/weather/<collection_name>', methods=['GET'])
def api(collection_name):
    rows = eval('db.' + collection_name)
    docs = {} #'{}' because we want to find all the collection
    results = find_docs_mongoDB(rows,docs)
    return jsonify(results)
    
if __name__ == '__main__':
    app.run(
	host="0.0.0.0",
        port=int("8080")
    )