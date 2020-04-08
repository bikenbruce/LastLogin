#!python
"""This script goes through the /Users directory in mac os and finds the
   last login for each one.  Then checks to see how long ago they logged in.
   The idea is to have a script that removes old accounts and files
   that have not been used in a period of time.  In this test case,
   we are looking at 30 days."""

import argparse
from common import UserRecordExists, DeleteUserRecord
from common import ArchiveHomeFolder, DeleteHomeFolder, UserHomeFolderExists
import datetime as dt
import dateutil.parser as dparser
import grp
import os
import socket
import subprocess

THIRTY_DAYS = dt.timedelta(days=30)
ADMINS = grp.getgrnam('admin').gr_mem

def check_local_users(days):
    """method to look at local users in /Users directory, and query the 'last'
       command to see when they last logged in."""

    days_ahead = dt.timedelta(days=days)

    for user in os.listdir("/Users"):
        if os.path.isdir(os.path.join("/Users", user)):
            # print(user)

            pipe = subprocess.run(
                ['/usr/bin/last', '-1', user],
                capture_output=True)

            output = pipe.stdout.strip().decode("utf-8")

            # print(output)

            if not output.strip().startswith('wtmp'):
                # print(output.strip())

                # if output contains login date / time range
                # example: Fri Sep 27 14:03 - 14:03
                if output.count(' - ') > 0:
                    last_log = output.split(' - ')[0].split('   ')[-1:][0]
                else:
                    # print(output)
                    last_log = output.replace('still logged in', '').\
                               strip().split('   ')[-1:][0]
                    # print(last_log)

                try:
                    # print(last_log)
                    last_log_time = dparser.parse(last_log, fuzzy=True)
                    today = dt.datetime.today()

                    if last_log_time > today:
                        last_log_time = last_log_time - dt.timedelta(days=365)

                    note = socket.gethostname().split('.')[0] + '-' +\
                           last_log_time.strftime("%Y-%m-%d")

                    print('user:', user, '\tlast_log_string:', last_log,
                          '\tlast_log_datetime:',
                          last_log_time.strftime("%a %b %_d, %Y %H:%M"))
                    if today - last_log_time > days_ahead:
                        print('\tgreater than 30 days')
                        if user not in ADMINS: 
                            ArchiveUser(user, note)
                        else:
                            print('\t', user, 'is an admin, not archiving account')

                except ValueError:
                    print(user, 'unable to extract date time')


def ArchiveUser(user, note=None):
    if UserRecordExists(user):
        print('\tUser record exists in Directory Service')
        if DeleteUserRecord(user):
            print('\tRemoved user record from Directory Service')
    else:
        print('\tUser record does not exist in Directory Service')

    if UserHomeFolderExists(user):
        print('\tUser home folder exists')
        if ArchiveHomeFolder(user, '/Users', note):
            print('\tUser home folder archived')
            if DeleteHomeFolder(user):
                print('\tUser home folder deleted')
        else:
            print('\tAttempted to archive users home folder')
    else:
        print('\tUser home folder does not exist')


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(
             description='show duration since last login for each user')
    PARSER.add_argument('-d', '--days', type=int, default=30,
                        help='number of days since last log in (defult: 30)')
    ARGS = PARSER.parse_args()

    check_local_users(ARGS.days)
