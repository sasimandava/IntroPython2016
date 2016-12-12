"""
Dec 11, 2016 test code for carrier_transid_count_refactor.py.
"""
import io
import os.path

from carrier_transid_count_refactor import carrier_transid_count, timed_func

def test_file_exists():
    assert os.path.isfile('/Users/Mandava/Documents/python/myprojects/final/server1/all_transids.txt') is True
    assert os.path.isfile('/Users/Mandava/Documents/python/myprojects/final/server2/log_data.txt') is True
    assert os.path.isfile('/Users/Mandava/Documents/python/myprojects/final/output.txt') is True

def test_transid_count():
    trans_file = "/Users/Mandava/Documents/python/myprojects/final/server1/all_transids_test.txt"
    log_file = "/Users/Mandava/Documents/python/myprojects/final/server2/log_data_test.txt"
    result = carrier_transid_count(trans_file, log_file)
    assert result == (20, 11, 11)

def test_exec_time():
    outfile = io.StringIO()
    with open('/Users/Mandava/Documents/python/myprojects/final/output.txt') as input:
        outfile = input.read()
    print(outfile)
    assert "Result: Total TIDs, Carrier Server1 Count, Carrier Server2 Count:" in outfile
    assert "time elapsed in minutes" in outfile

def test_file_exception():
    trans_file = "/Users/Mandava/Documents/python/myprojects/final/server1/all_transids_test1.txt"
    log_file = "/Users/Mandava/Documents/python/myprojects/final/server2/log_data_test.txt"
    try:
        result = carrier_transid_count(trans_file, log_file)
    except (FileNotFoundError) as error:
        result = error.args[1]
        print('error.args[1]')
        assert 'No such file or directory' == result

# def test_decorator():
#     timed_func((lambda x: x**2)(100000))
#     outfile = io.StringIO()
#     with open('/Users/Mandava/Documents/python/myprojects/final/output.txt') as input:
#         outfile = input.read()
#     print(outfile)
#     assert "time elapsed" in outfile
