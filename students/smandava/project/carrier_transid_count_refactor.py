#!/usr/bin/env python3

"""
Project description:
[1] File1 contains transaction IDs (from a log file) from server1. File size ~24K.
[2] File2 contains log data from server2. Every line in the log data on server2 does not have to contain transaction IDs from step1. File size ~480MB.
[3] Search for the occurrences of transaction IDs from server1 and IP address1 in the server2's log data and get final count.
[4] Search for the occurrences of transaction IDs from server1 and IP address2 in the server2's log data and get final count.
[5] Verify the counts in step 3 and step4 match.
[6] Use decorators or context managers.
"""
import time
"""
Decorator function to calculate the execution time.
"""
def timed_func(carrier_transid_count):
    def timed(*args, **kwargs):
        start = time.time()
        result = carrier_transid_count(*args, **kwargs)
        elapsed = (time.time() - start) / 60
        with open("/Users/Mandava/Documents/python/myprojects/final/output.txt", 'w') as output:
            output.write("Result: Total TIDs, Carrier Server1 Count, Carrier Server2 Count: {}\ntime elapsed in minutes: {} \n".format(result, elapsed))
        # print("time expired: {} in minutes".format(elapsed))
        return result
    return timed


@timed_func
def carrier_transid_count(trans_file, log_file):
    """Function to count the transaction IDs from server1 in server 2's logfile."""
    total_tids = 0
    server1_count = 0
    server2_count = 0
    with open(trans_file) as trans_file, open(log_file, encoding="utf-8", errors="ignore") as log_file:
        """Ignore the errors encountered with parsing of characters like ±."""
        logfile_split = log_file.read().splitlines()
        for tid in trans_file:
            total_tids += 1
            for log_entry in logfile_split:
                log_entry.strip()
                tid.strip()
                if (tid.strip() in log_entry.strip() and ("66.94.10.196") in log_entry.strip()):
                    server1_count += 1
                if (tid.strip() in log_entry.strip() and ("66.94.27.196") in log_entry.strip()):
                    server2_count += 1
                else:
                    continue
                continue
    return (total_tids, server1_count, server2_count)
    # print("Total TIDs:", total_tids)
    # print("Carrier Server1 Count:", server1_count)
    # print("Carrier Server2 Count:", server2_count)

"""
Timer class is for using context manager.
Uncomment the Timer class code and comment timed_func decorator code to use context manager.
"""

# class Timer:
#     def __init__(self, outfile=sys.stdout):
#         self.outfile = outfile

#     def __enter__(self):
#         self.start = time.time()

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # print("elapsed time:", time.time - self.start)
#         self.outfile.write("elapsed time: {} minutes \n".format((time.time() - self.start)/60))

if __name__ == "__main__":
    trans_file = "/Users/Mandava/Documents/python/myprojects/final/server1/all_transids.txt"
    log_file = "/Users/Mandava/Documents/python/myprojects/final/server2/log_data.txt"
    try:
        carrier_transid_count(trans_file, log_file)
    except(FileNotFoundError) as error:
        # print(dir(error))
        with open("/Users/Mandava/Documents/python/myprojects/final/output.txt", 'w') as output:
            output.write("File not found: {} \n".format(error.filename))
    """Code to execute when using context manager."""
    # with Timer() as t:
    #     carrier_transid_count()
