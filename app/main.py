from singupy import api as singuapi
import os
import sys
import pandas as pd
from time import sleep
#import requests

path1 ="/app/dlr_mrid.csv"


def clean_file(file_loc):
    #read file and remove white space
    data = pd.read_csv(file_loc,delim_whitespace=True,on_bad_lines = 'skip')
    #remove line 1 "----" and last " xx row effectd " from SQL export file
    data.drop(data.head(1).index,inplace=True)
    data.drop(data.tail(1).index,inplace=True)
    return data


def main():
    if (os.path.isfile(path1)):
        print("file exists as", path1)
    else:
        print("no file exists as", path1)
        sys.exit()
    
    dataframe = clean_file(path1)    
    my_api = singuapi.DataFrameAPI(dataframe, dbname = 'SEG_MEAS_MRID')   
    while(True):
      my_api['SEG_MEAS_MRID'] = clean_file(path1)
      sleep(5)


if __name__ == "__main__":
    main()
     

     
 
    
