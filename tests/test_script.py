import pytest
import app.main
import pandas as pd
import os


# Dummytest which will always succeed - must be replaced by real tests
def test_dummy():
    assert True

#non-function test ,special for DLR requirement, don't genral purpose code run.  
def test_file_header():
    path = f"{os.path.dirname(os.path.realpath(__file__))}/dlr_mrid_PROD.csv"
    colon1 = "AMPS_MRID"
    colon2 = "LINESEGMENT_MRID"
    colon3 = "DLR_ENABLE"
    #dataframe = app.main.clean_file(path)
    dataframe = pd.read_csv(path,delimiter=",",on_bad_lines = 'skip')
    my_list = list(dataframe)
    assert colon1 in my_list
    assert colon2 in my_list
    assert colon3 in my_list

def test_clean_file():
    path = f"{os.path.dirname(os.path.realpath(__file__))}/dlr_mrid_PROD.csv"
    dataframe = app.main.clean_file(path)
    colon1 = "-----"
    if colon1 in dataframe.iloc[1]:
        assert False
    else:
        assert True




