import extract
import config
import transform
import load
import pandas as pd
import os
import json

#Data Extraction based on city list

extract.get_air_quality_data(config.city_list)



#Data Transformation
transform.transform('extract/berlin.json')


#Combining all json files from the transform folder before loading as a jason
list_of_json_files=os.listdir('transform/')
df = pd.DataFrame() 
for i in list_of_json_files:
    #print(i)
    with open('transform/'+i, 'r') as f:
      data = json.load(f)
    data1=pd.DataFrame.from_dict(data)
    df=df.append(data1)
df.to_json('berlin.json',orient="records") #Saving combination of all json in the working directoy as rename as 'berlin.json'.


#Load data to the database 
data=pd.read_json('berlin.json')
db_object=load.Db()
db_object.load_to_db('berlin',data)