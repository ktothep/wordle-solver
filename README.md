# wordle-solver-5-letter
Set of API's which you can call to solve  your Wordle Puzzle

Pre-Requisite:
MongoDB instance up and running on your local system.If not on your local system then you have to make changes to the connection parmaeter in the files.

Initial-Setup:

1.Execute the File wordinserter.py to create a database of 5 letter words in your MongoDB.On successful execution you will find  DB words with collection name 
fiveletter

2.Start the wordleapi.py file.By default the port for running the API is 5000

API's:
**/startswith/<string:letters>:** Returns a list of words which start with the string given by you

**/endswith/<string:letters>:** Returns a list of words which end with the string given by you

**/contains/<string:letters>:** Returns a list of words which contain the string given by you

**/noletter?with=<param1>&without=<param2>:** Returns a list of words which have letters given inparam1 and do not have letters given in param2
