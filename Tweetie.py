import json
import pprint
import requests
from requests_oauthlib import OAuth1
#######################RESOURCES###############################################
#-------------ABOUT oauth-------------------------------------------------------
#https://stackoverflow.com/questions/26965624/cant-import-requests-oauthlib
#http://docs.python-requests.org/en/master/user/authentication/
#https://stackoverflow.com/questions/16521486/tutorial-for-using-requests-oauth2
#-------------------------------------------------------------------------------

#------------Twitter API reference----------------------------------------------
#https://developer.twitter.com/en/docs/api-reference-index
#-------------------------------------------------------------------------------

#-------------------Resources----\----------------------------------------------

#http://www.mikaelbrunila.fi/2017/03/27/scraping-extracting-mapping-geodata-twitter/
#https://knightlab.northwestern.edu/2014/03/15/a-beginners-guide-to-collecting-twitter-data-and-a-bit-of-web-scraping/
#http://thepythondjango.com/scraping-10000-tweets-in-60-seconds-using-celery-rabbitmq-and-docker-clusterwith-rotating-proxy/

################################################################################

#-------------------------------Twitter auth------------------------------------
CONSUMER_KEY = 	'<your key>'
CONSUMER_SECRETS = 	'<your consumer secrets>'
A_TOKEN = '<your auth token>'
A_TOKEN_SECRET = '<your auth token secret>'
#-------------------------------------

#--------------------Authentication process-------------------------------------
#if we look at the url we see ---------------------------------->screen_name=
#the screen_name is just the screen name of the person whose tweets we want to search
url2 = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=SamGolbach&count=2'
#------this is a requests object containing our data to authenticate into Twitter
my_auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRETS,A_TOKEN, A_TOKEN_SECRET)

#-------------------------------------------------------------------------------
auth = requests.get(url2, auth=my_auth) #this is our GET request to "get"
                                        #info from the server
auth.status_code  # this is a numeric code that lets us know the status of our
                  # request. Check below for more info on status codes
                  # http://www.restapitutorial.com/httpstatuscodes.html

pythonFormat = auth.json() #this is the JSON response from the server
pprint.pprint(pythonFormat) # here we print the JSON response to the command line
#--------------Converts JSON to Python------------------------------------------
