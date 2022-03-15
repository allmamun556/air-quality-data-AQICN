# air-quality-data-AQICN
Step 1: write a main() function that will  that will extract, transform and load data to te postgres database.( just work with only one city)

step 2: each times after running the main it will merge with the previoud data( just marge always-- dont need to check data reduntancy)

step 3: Use air flow means that will main function will run automatacillay with a interval of time and merge the data using airflow

step 4: Dockerize this ETL application

step 5: Implement some CI/CD pipeline

step 6: Implent this things using amazaon s3 bucket

step 7: Using Amazon Redshefit after the S3

step 8: Give a OOP structe for this ETL piple line



##############To be Remember########
" from etl.load import * 

----" The meaning of this import is it will import all methods and attribute from the load module which is loacted inside 
      the etl directory.
---- The import is done in any modules which is top of the "etl" directory.
---- Then, to use the methods and attribute , don't need to use the module name in front of the methods or attributes.
---- for  example: load.('method or attribute name"
---- call the methods or attribute directly whitout referencing the modules name. 


"from etl import load "
--- Here it imports the "load" modules.Then to use the methods or attributes from the "load" modules 
---you have to put the modules name before the attribute or methods before calling them.
--- example: "load.(methods or attributes name)"

" from .config import *
-----To import all from the "config" modules.
-----The place of importing and the config modules  are in the same levels
 N.B: for building etl pipeline, you have to import  like this "from .config import * " in any files inside the etl directory.
Then if you use thes modules top of the etl directory it would be imported automaticayll; when you import the modules which import like this.


Importing things: For making etl pipeline follow this  structure if you want to use functional programming rather objectt oriented programming.
For the better understanding  see the code levels of this directory.
