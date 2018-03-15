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
################################################################################

#-------------------------------Twitter auth------------------------------------
CONSUMERKEY = 	'<your key>'
CONSUMERSECRETS = 	'<your consumer secrets>'
AUTH_TOKEN = '<your auth token>'
AUTH_TOKEN_SECRET = '<your auth token secret>'
#-------------------------------------

#--------------------Authentication process-------------------------------------
url2 = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=SamGolbach&count=2'
my_auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRETS,A_TOKEN, A_TOKEN_SECRET)
#-------------------------------------------------------------------------------
auth = requests.get(url2, auth=my_auth)
auth.status_code
pythonFormat = auth.json()
pprint.pprint(pythonFormat)
#--------------Converts JSON to Python------------------------------------------
