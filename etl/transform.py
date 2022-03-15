import json
import pandas as pd
#from .util import *
''' This means  it will impor everything from the util modules. and here transform and util modules are in same level.
Thats why . is used '''
#from .util import *
#from util import KeyError_handling_iaqi_wg_v

#mporting datetime module for now() 
from datetime import datetime
    
# using now() to get current time 
current_time = datetime.now()
current_time = current_time.strftime("%H:%M:%S")
#current_time

def KeyError_handling_iaqi_wg_v(data):
    try:
        data_=data['iaqi']['wg']['v']
    except KeyError:
        print("no data is found for iaqi_wg_v")

    finally:
        data_=None

        #return  data_
    return data_

#KeyError_handling_iaqi_wg_v(data)


def transform(dir):
    '''This function reads the extract files from the extract folder.
    Then it transform it and save it in the transform directory inside the etl directory.
    when saves it includes the current time with the file name.'''
    with open(dir) as f:
     data = json.load(f)
    keys=['iso','city_name','aqi','idx','h','no2','p','pm25','t','w','wg','s','tz','v']
    values=[data['time']['iso'],
    data['city']['name'],
    data['aqi'],
    data['idx'],
    data['iaqi']['h']['v'],
    data['iaqi']['no2']['v'],
    data['iaqi']['p']['v'],
    data['iaqi']['pm25']['v'],
    data['iaqi']['t']['v'],
    data['iaqi']['w']['v'],
    KeyError_handling_iaqi_wg_v(data),
    data['time']['s'],
    data['time']['tz'],
    data['time']['v']
    ]
    dictionary = dict(zip(keys, values)) 
    data=pd.DataFrame(dictionary,index=keys)
    data=data.head(1)
    data=data.reset_index(drop=True)
    return data.to_json('etl/'+'transform/'+str(current_time).replace(':','_')+('_')+'berlin.json')

#transform('etl/'+'extract/berlin.json')




