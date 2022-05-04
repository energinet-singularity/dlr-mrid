import pytest
import app.main
import pandas as pd
import os


# non-function test ,special for DLR requirement, don't genral purpose code run.
def test_file_header():
    path = f"{os.path.dirname(os.path.realpath(__file__))}/valid-testdata/test_data.csv"
    colon1 = "AMPS_MRID"
    colon2 = "LINESEGMENT_MRID"
    colon3 = "DLR_ENABLE"
    dataframe = pd.read_csv(path, delimiter=",", on_bad_lines='skip')
    my_list = list(dataframe)
    assert colon1 in my_list
    assert colon2 in my_list
    assert colon3 in my_list


def test_clean_file():
    path = f"{os.path.dirname(os.path.realpath(__file__))}/valid-testdata/test_data.csv"
    dataframe = app.main.clean_file(path)
    colon2 = "-----"
    if colon2 in dataframe.iloc[1]:
        assert False
    else:
        assert True


def test_dataframe():
    expected_dict = {'TERMINAL_EMSNAME': ['Dummy_line', 'Dummy_line'],
                      'FAR_NEAR': ['N', 'F'],
                      'AMPS_MRID': ['12345678-1234-abcd-efgh-123456789abc', '12345678-1234-abcd-efgh-123456789def'],
                      'LINESEGMENT_MRID': ['12345679-4567-ijkl-5678-123456789abc', '12345679-4567-ijkl-5678-123456789abc'],
                      'DLR_ENABLE': ['NO', 'YES']}
    expected_frame = pd.DataFrame.from_dict(expected_dict)
    path = f"{os.path.dirname(os.path.realpath(__file__))}/valid-testdata/test_data.csv"
    dataframe = app.main.clean_file(path)
    assert dataframe.equals(expected_frame)
