# Generic modules
import os
import time
import logging
from time import sleep


# Modules
from singupy import api as singuapi
import pandas as pd

# Initialize log
log = logging.getLogger(__name__)

def clean_file(file_loc: str) -> pd.DataFrame:
    """ Read file from file_loc and remove 1 data line "-----"

    Parameters
    ----------
    file_loc : str
      full string path for file

    Returns
    -------
    dataframe
      pandas dataframe.

    Example
    ------
        >>> dataframe = clean_file("/home/dat_file.csv")
    """
    data = pd.read_csv(file_loc, delimiter=",", on_bad_lines='skip', encoding='cp1252')
    data.drop(data.head(1).index, inplace=True)
    data.reset_index(drop=True, inplace=True)
    return data


def main():
    old_stamp = None
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    # Load filename if defined - or use default value
    x = os.environ.get('file_name')
    if x is not None:
        filepath_csv = "/data/" + x
        while not os.path.isfile(filepath_csv):
            log.info(f"file not found will keep try every 30 sec")
            sleep(30)
    elif os.environ.get('use_mock_data', 'FALSE').upper() == 'FALSE':
        filepath_csv = "/test_data/test_data.csv"
    else:
        filepath_csv = "/test_data/mock_dlr_mrid_PROD.csv"
        

    # if enviroment varible not define database_expose get default database name
    if 'database_expose' in os.environ:
        database_expose = os.environ.get('database_expose')
        log.info(database_expose)
    else:
        database_expose = "SEG_MEAS_MRID"

    # enviroment varible should be greated then 10 sec and less then 30 days else it get 15 min default
    try:
        if 10 < int(os.environ.get('cycle_time')) < 60*60*24*30:
            cycle_time = int(os.environ.get('cycle_time'))
        else:
            cycle_time = 900
    except Exception:
        cycle_time = 900
        log.info(f" run with default cycle : {cycle_time}")

    try:
        os.path.isfile(filepath_csv)
        log.info(f"file exists as : {filepath_csv} ")
    except Exception as e:
        log.info(f"File '{filepath_csv}' was not found")
        log.exception(f" reading file Failed with the message: '{e}'")


    log.info(f"file read time in sec: {cycle_time}")
    my_api = singuapi.DataFrameAPI()
    while(True):
        new_stamp = time.ctime(os.path.getmtime(filepath_csv))
        if (new_stamp != old_stamp):
            my_api[database_expose] = clean_file(filepath_csv)
            old_stamp = new_stamp
        time.sleep(cycle_time)


if __name__ == "__main__":
    main()
