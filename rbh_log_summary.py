# coding: utf-8
''' Generates summary reports from Robin Hood log files. '''

import argparse
import re
import sys

from humansize import approximate_size


if __name__ == '__main__':

    # Set up the regexes
    re_filename = re.compile(r".*Purged '([^']+)'")
    re_bytes = re.compile(r".*size=(\d+)")
    re_atime = re.compile(r".*last access (\d+\.\d+)")

    # command-line args
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='verbose output', action='store_true')
    parser.add_argument('-a', '--atime_threshold', default=30.0, type=float)
    parser.add_argument('log_file')
    args = parser.parse_args()

    # report variables
    total_bytes = 0.0
    bad_log_lines = 0
    total_files = 0

    # parse the log line by line
    with open(args.log_file) as f:
        for line in f:
            try:
                size_bytes = (int)(re_bytes.match(line).group(1))
                atime = (float)(re_atime.match(line).group(1))

                if atime >= args.atime_threshold:
                    total_bytes += size_bytes
                    total_files += 1

            except:
                if args.verbose:
                    e = sys.exc_info()[0]
                    print('Error parsing line {0}:\n\t{1}'.format(line, e))

                bad_log_lines += 1
                continue

    # Final report
    print('Source log file: {0}'.format(args.log_file))
    print('Bad log lines (skipped): {0}'.format(bad_log_lines))
    print('Threshold: {0} days'.format(args.atime_threshold))
    print('File count: {0}'.format(total_files))
    print('Total freed: {0}'.format(approximate_size(total_bytes)))
