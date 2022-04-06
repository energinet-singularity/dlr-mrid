from singupy import api as singuapi
import os
import sys
import pandas as pd
from time import sleep
#import requests

#enviroment varible for filename
try:
    os.environ.get('file_name')
    path1 = "/app/" + str(os.environ.get('database_expose'))
except:
    path1 ="/app/dlr_mrid_PROD.csv"

#enviroment varible should be greated then 10 sec and less then 30 days else it get 15 min default
try:
    os.environ.get('cycle_time')
    if 10 < int(os.environ.get('cycle_time')) < 108720:
        cycle_time = int(os.environ.get('cycle_time'))
except:
    cycle_time = 900

# if enviroment varible not define database_expose get default database name
try:
    os.environ.get('database_expose')
    database_expose = str(os.environ.get('database_expose'))
except:
    database_expose = "SEG_MEAS_MRID"


def clean_file(file_loc):
    data = pd.read_csv(file_loc,delimiter=",",on_bad_lines = 'skip')
    #remove line 1 "----" from SQL export file
    data.drop(data.head(1).index,inplace=True)
    return data

def main():
    if (os.path.isfile(path1)):
        print("file exists as", path1)
    else:
        print("no file exists as", path1)
        sys.exit()    
    dataframe = clean_file(path1)    
    my_api = singuapi.DataFrameAPI(dataframe, dbname = database_expose)
    while(True):
      my_api[database_expose] = clean_file(path1)
      sleep(cycle_time)


if __name__ == "__main__":
    main()
     

     
 
    
