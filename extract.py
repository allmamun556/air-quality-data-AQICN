import requests
import json

def get_air_quality_data(city, accesstoken='7672327f1d6675ef5d2d554b63b6175afec9fe77'):
    # build request
    url = 'http://api.waqi.info/feed/'+city+'/?token=' + accesstoken
    # get data
    r = requests.get(url, auth=('user', 'pass'))
    # check status code and return data
    if r.status_code == 200:
        data = r.json()
        data=data['data']
        with open('extract'+'/'+city+'.'+'json', 'w') as fp:
         json.dump(data, fp)

        #return json.dumps(data)


city_list=['berlin','newyork','seoul']
#print(type(get_air_quality_data('berlin')))
#print(json.dumps(get_air_quality_data('berlin')))
#print(json.dumps(get_air_quality_data('newyork')))
#print(json.dumps(get_air_quality_data('newyork')))
#print(json.dumps(get_air_quality_data('seoul')))

for i in city_list:
    get_air_quality_data(i)


#import json

