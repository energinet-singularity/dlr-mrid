from singupy import api as singuapi
import os
import sys
import pandas as pd
from time import sleep
#import requests

file_name = "dlr_mrid_PROD.csv"
path1 ="/app/" + file_name
cycle_time = 900
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
     

     
 
    
