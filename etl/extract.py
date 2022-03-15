import requests
import json
from .config import *

def get_air_quality_data(city=city_list, accesstoken=access_token):
    ''' This function extract the air quality data from the  wevsites.
    Then store this extracted data in the extract folder inside  the etl directory.'''
    # build request
    url = base_url+city+'/?token=' + accesstoken
    # get data
    r = requests.get(url, auth=('user', 'pass'))
    # check status code and return data
    if r.status_code == 200:
        data = r.json()
        data=data['data']
        with open('etl/'+'extract'+'/'+city+'.'+'json', 'w') as fp: #to write data
         json.dump(data, fp)

       
#get_air_quality_data()

