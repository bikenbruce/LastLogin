#!python
from common import UserRecordExists, DeleteUserRecord
from plistlib import *
import datetime as dt
import os


def GetUsersPlist():
    users = {}
    for user in os.listdir("/Users"):
        user_home_path = '/Users/' + user
        user_plist = os.path.join(
            user_home_path,
            "Library/Preferences/com.trusourcelabs.NoMAD.plist")
        if os.path.isfile(user_plist):
            users.update({user: user_plist})
    return(users)


def CheckUserState(user, user_plist):
    today = dt.datetime.today()

    with open(user_plist, 'rb') as fp:
        nomad_plist = load(fp)
        if 'LastPasswordExpireDate' in nomad_plist:
            print('user:', user, '\texpire date:',
                  str(nomad_plist['LastPasswordExpireDate'].date()), end='')

            if nomad_plist['LastPasswordExpireDate'] > today:
                print('\tstate: not expired')
            else:
                print('\tstate: expired')
                RemoveUser(user)


def RemoveUser(user):
    if UserRecordExists(user):
        if DeleteUserRecord(user):
            print('\tRemoved user record from Directory Service')
        else:
            print('\tUnable to remove user record from Directory Service')
    else:
        print('\tUser record does not exist in Directory Service')


if __name__ == "__main__":
    users = GetUsersPlist()
    for user, plist in users.items():
        CheckUserState(user, plist)
