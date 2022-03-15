from etl import extract
from etl import transform
from etl import load
#from etl import load 
#from etl import util
#from etl import load
#from etl.util import *



def main():
  #Data Extraction based on city list
  extract.get_air_quality_data()
  print('Data extraction is done successfully')



  #Data Transformation
  transform.transform('etl/'+'extract/berlin.json')

  print('Transformation is done successfully')


  load.combine_and_load_to_db() # this comes from the python load modules of etl directory



main()