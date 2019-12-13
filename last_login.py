#!/usr/bin/env python
"""This script goes through the /Users directory in mac os and finds the last login for
   each one.  Then checks to see how long ago they logged in.  The idea is to have a
   script that removes old accounts and files that have not been used in a period of time.
   In this test case, we are looking at 30 days."""

from subprocess import Popen, PIPE, STDOUT
import argparse
import os
import datetime as dt
import dateutil.parser as dparser

TODAY = dt.datetime.today()
THIRTY_DAYS = dt.timedelta(days=30)

def check_local_users(days):
    """method to look at local users in /Users directory, and query the 'last' command
       to see when they last logged in."""

    days = dt.timedelta(days=days)

    for user in os.listdir("/Users"):
        if os.path.isdir(os.path.join("/Users", user)):
            # print(user)

            pipe = Popen(
                ['/usr/bin/last', '-1', user],
                stdin=PIPE, stdout=PIPE, stderr=STDOUT)

            # python 3 note:
            # need to add .decode("utf-8")
            output = pipe.communicate()[0].strip().decode("utf-8")

            # print(output)

            if not output.strip().startswith('wtmp'):
                # print(output.strip())

                # if output contains login date / time range
                # example: Fri Sep 27 14:03 - 14:03
                if output.count(' - ') > 0:
                    last_log = output.split(' - ')[0].split('   ')[-1:][0]
                else:
                    # print(output)
                    last_log = output.replace('still logged in', '').strip().split('   ')[-1:][0]
                    # print(last_log)

                try:
                    # print(last_log)
                    last_log_time = dparser.parse(last_log, fuzzy=True)

                    print('user:', user, '\tlast_log:', last_log, '\tlast_log_time:', last_log_time)
                    if TODAY - last_log_time > days:
                        print('greater than 30 days')
                    print("")
                except ValueError:
                    print(user, 'unable to extract date time')


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='show users that have not logged in')
    PARSER.add_argument('-d', '--days', type=int, default=30,
                        help='number of days since last log in (defult: 30)')
    ARGS = PARSER.parse_args()

    check_local_users(ARGS.days)
