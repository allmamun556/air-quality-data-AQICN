#import db
import psycopg2
#from simplejson import load
from sqlalchemy import create_engine
#from .transform import BaseTransformer
import json
import pandas as pd
import glob
#import pprint as pp #Pretty printer
from .config import *
#import config
import os



class Db:
    def load_to_db(self,table_name, dataframe):
        #engine=create_engine(engine)
        engine = create_engine(f'postgresql://{database_username}:{database_password}@localhost/{database_name}')
        dataframe.to_sql(table_name, engine, if_exists='replace',
                index=False)




    #from sqlalchemy import create_engine

    #df.to_sql('table_name', engine)





    def read_from_db(self,sql_query, conn_string):
        #conn_string=ConfigReader()
        #conn_string=conn_string.configuration() 
        conn = psycopg2.connect(conn_string)

        #Setting auto commit false
        conn.autocommit = True

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        #Retrieving data
        cursor.execute(sql_query)

        #Fetching 1st row from the table
        result = cursor.fetchone();
        print(result)

        #Fetching 1st row from the table
        result = cursor.fetchall();
        print(result)

        #Commit your changes in the database
        conn.commit()

        #Closing the connection
        conn.close()





    
#Combining all json files from the transform folder before loading as a jason
def combine_all_json_from_transform_folder():
    ''' This function  read all json files from the  transforl folder then combine all json together.
    and then save it to above of the etl directory as 'berlin.json' '''
    list_of_json_files=os.listdir('etl/transform/')
    df = pd.DataFrame() 
    for i in list_of_json_files:
        #print(i)
        with open('etl/transform/'+i, 'r') as f:
            data = json.load(f)
        data1=pd.DataFrame.from_dict(data)
        df=df.append(data1)
    df.to_json('berlin.json',orient="records") #Saving combination of all json in the working directoy as rename as 'berlin.json'.


#combine_all_json_from_transform_folder()

#print('Data load to the postgres database is done successfully')



def load_json_files_as_dataframe_to_sql_database():
    '''This function read the berlin.json files from the root directory.
    then load it to the database'''
    with open('berlin.json','r') as wp:
        data=json.load(wp)
    data=pd.DataFrame.from_dict(data)
    db_object=Db()
    db_object.load_to_db('berlin',data)

#load_json_files_as_dataframe_to_sql_database()


def combine_and_load_to_db():
    combine_all_json_from_transform_folder()
    load_json_files_as_dataframe_to_sql_database()
    print('Data is load to the database successfully')

#combine_and_load_to_db()
