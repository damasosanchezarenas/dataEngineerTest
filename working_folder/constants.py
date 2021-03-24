"""
Created on March 2021 by Damaso Sanchez Arenas.

File where you can put all the constants of the proyect
"""

#CONSTANTS
CITIES = ['London', 'Madrid', 'Boston']
URI = 'https://www.metaweather.com'
HEADER = {'Content-Type':'application/json'}

#PATHS
WORKING_PATH = r'C:\Users\jesus\CW\data-engineer-exercise\working_folder'
FILE_CONFIG_PATH = r'C:\Users\jesus\cw\data-engineer-exercise\working_folder\config.ini'
FILE_LOG_PATH = r'C:\Users\jesus\cw\data-engineer-exercise\working_folder\logger.log'

#MESSAGES
CVS_GENERATED_STR = 'Everything went well :)\nThe .csv have been generated in the path: '
WOEID_STR = 'The woeid of '
SAVE_DATA_STR= 'The file has been saved in Mongo Database'
CONNECTION_ERROR_STR = 'Connection error with Mongo Atlas'
CONNECTED_STR = "****YOU ARE CONNECTED WITH THE API****"
CONNECT_TO_API_STR = '1. Browser ==> http://localhost:8080/api/weather/<City>'
CONSOLE_TO_API_STR = '2. Console ==> request.get(http://localhost:8080/api/weather/<City>)'
EXIT_STR='3. To exit ==> Ctrl+c\n\n'
WINDOWS_STR = 'You have Windows :)'
LINUX_STR = 'You have Linux :)'
ARROW_STR = ' ==> '
END_LINE = '\n\n'

