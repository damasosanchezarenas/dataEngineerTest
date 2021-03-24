Hello I am Damaso :)

-In the working folder we have the following files:


1. readApi.py ==> This script reads the information from the api ('https://www.metaweather.com')
				  and generates the different .csv with the forecast of the following days (consolidated_weather) 
				  for the selected cities. In my case, the chosen cities have been: Madrid, Boston and London.

2. saveData.py ==> In this script we save the information from the previously generated .csv in a mongoDB Atlas database.

3. commonsFunctions.py ==> In this script we have different common functions that help us achieve the desired functionalities 
						   and that could be useful at another time.

4. constants.py ==> In this file we have all the constants of the project.
					Paths, messages, cities, etc.

5. config.ini ==> In this file we have the configuration information of the mongo db database.


6. explanation6.txt ==> In this file we have the explanation of how I made the optional number 6.


Also if you run the different .py files you will see the logger of the different processes and the generated .csv.



-Inside the folder we have a subdirectory called app where the api.py file is located:

1. api.py ==> Flask process that connects us on our localhost with the data previously stored in the MongoDB database.
		      To test it, you must run the script ($ python api.py) and put the following in the browser:
		      http://localhost:8080/api/weather/<City>


-In the optional6 folder found in the working_folder directory we can find:

1. script. sh ==> Very simple script that executes the .py made previously together.
				  This will be the script the crontab will call.

2. crontab ==> Crontab that makes the script run every day at 2.30 everyday.

3. dockerfile ==> Dockerfile to be able to create the docker image that executes the crontab 
				  and therefore the script daily.

4. cron.log ==> Log where you can see the times where the script is executing.sh


Thanks :)

Damaso. 