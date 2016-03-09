# coding: utf-8

import re


# Define the human-readable approximate size function, from Dive into Python 3

# Set up the regexes
re_filename = re.compile(r".*Purged '([^']+)'")
re_bytes = re.compile(r".*size=(\d+)")
re_atime = re.compile(r".*last access (\d+\.\d+)")

# values that could come from command-line args
file = './askap_purge'
atime_threshold = 30.0
verbose = True

# report variables
total_bytes = 0.0
bad_log_lines = 0
total_files = 0

# parse the log line by line
with open(file) as f:
    for line in f:
        try:
            size_bytes = (int)(re_bytes.match(line).group(1))
            atime = (float)(re_atime.match(line).group(1))

            if atime >= atime_threshold:
                total_bytes += size_bytes
                total_files += 1

            if verbose:
                filename = re_filename.match(line).group(1)
                print('{0}: {1} bytes, last access: {2} days'.format(filename, size_bytes, atime))
        except e:
            bad_log_lines++
            continue


# Final report
print('Source log file: {0}'.format(file))
print('Bad log lines (skipped): {0}'.format(bad_log_lines))
print('Threshold: {0} days'.format(atime_threshold))
print('File count: {0}'.format(total_files))
print('Total freed: {0}'.format(total_bytes))

