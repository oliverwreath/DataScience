import json 
import requests 
import pprint 

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    #print url 
    data = requests.get(url).text
    data = json.loads(data)
    #print type(data)
    #print data['topartists']['artist'][0]['name']

    
    return data['topartists']['artist'][0]['name'] # return the top artist in Spain





