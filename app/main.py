from singupy import api as singuapi
import os
import sys
import pandas as pd
import time


#enviroment varible file cleanup to remove 2 line "---""
def clean_file(file_loc):
    data = pd.read_csv(file_loc, delimiter=",", on_bad_lines='skip')
    data.drop(data.head(1).index, inplace=True)
    return data


def main():
    old_stamp = 'init'
    #enviroment varible for filename
    if os.environ.get('file_name'):
        filepath_csv = "/app/" + str(os.environ.get('file_name'))
    else:
        filepath_csv = "/app/dlr_mrid_PROD.csv"

    # if enviroment varible not define database_expose get default database name
    if os.environ.get('database_expose'):
        database_expose = str(os.environ.get('database_expose'))
    else:
        database_expose = "SEG_MEAS_MRID"

    #enviroment varible should be greated then 10 sec and less then 30 days else it get 15 min default
    try:
        os.environ.get('cycle_time')
        if 10 < int(os.environ.get('cycle_time')) < 108720:
            cycle_time = int(os.environ.get('cycle_time'))
        else:
            cycle_time = 900
    except Exception as e:
        cycle_time = 900

    if (os.path.isfile(filepath_csv)):
        print("file exists as", filepath_csv)
    else:
        print("no file exists as", filepath_csv)
        sys.exit()

    print("file read time in sec=", cycle_time)
    print("database expose=", database_expose)
    dataframe = clean_file(filepath_csv)
    my_api = singuapi.DataFrameAPI(dataframe, dbname=database_expose)
    while(True):
        new_stamp = time.ctime(os.path.getmtime(filepath_csv))
        if (new_stamp != old_stamp):
            my_api[database_expose] = clean_file(filepath_csv)
        old_stamp = new_stamp
        time.sleep(cycle_time)


if __name__ == "__main__":
    main()
