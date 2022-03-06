import json
#import json
import pandas as pd
import utils






def transform(dir):

    with open(dir) as f:
     data = json.load(f)



    keys=['iso','city_name','aqi','idx','h','no2','p','pm25','t','w','wg','s','tz','v']
    values=[data['time']['iso'],
    data['city']['name'],
    data['aqi'],
    data['idx'],

    #data['city']['geo'
    data['iaqi']['h']['v'],
    data['iaqi']['no2']['v'],
    data['iaqi']['p']['v'],
    data['iaqi']['pm25']['v'],
    #print(data['iaqi'])
    data['iaqi']['t']['v'],
    data['iaqi']['w']['v'],
    utils.KeyError_handling_iaqi_wg_v(data),
    data['time']['s'],
    data['time']['tz'],
    data['time']['v']
    ]


    dictionary = dict(zip(keys, values)) 
    data=pd.DataFrame(dictionary,index=keys)

    data=data.head(1)
    data=data.reset_index(drop=True)
    #print(data)
    return data.to_json('transform/'+dir)


transform('newyork.json')
transform('berlin.json')
transform('seoul.json')

