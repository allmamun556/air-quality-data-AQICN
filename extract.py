import requests
import json
import config

def get_air_quality_data(city, accesstoken=config.access_token):
    # build request
    url = config.base_url+city+'/?token=' + accesstoken
    # get data
    r = requests.get(url, auth=('user', 'pass'))
    # check status code and return data
    if r.status_code == 200:
        data = r.json()
        data=data['data']
        with open('extract'+'/'+city+'.'+'json', 'w') as fp: #to write data
         json.dump(data, fp)

       
#get_air_quality_data(config.city_list)




