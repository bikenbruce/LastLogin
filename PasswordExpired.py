#!python
"""This script looks at each user account found in the /Users folder.
   If the account has used NoLo / NoMAD Login, a plist file will contain
   information about the account and when the password will expire.
   If the password has expired, the user record found in directory 
   services will be deleted.
   """

from common import UserRecordExists, DeleteUserRecord
from plistlib import load
import datetime as dt
import os


def GetUsersPlist():
    users = {}
    for user in os.listdir("/Users"):
        user_home_path = "/Users/" + user
        user_plist = os.path.join(
            user_home_path, "Library/Preferences/com.trusourcelabs.NoMAD.plist"
        )
        if os.path.isfile(user_plist):
            users.update({user: user_plist})
    return users


def CheckUserState(user, user_plist):
    today = dt.datetime.today()

    with open(user_plist, "rb") as fp:
        nomad_plist = load(fp)
        if "LastPasswordExpireDate" in nomad_plist:
            print(
                "user:",
                user,
                "\texpire date:",
                str(nomad_plist["LastPasswordExpireDate"].date()),
                end="",
            )

            if nomad_plist["LastPasswordExpireDate"] > today:
                print("\tstate: not expired")
            else:
                print("\tstate: expired")
                RemoveUserRecord(user)


def RemoveUserRecord(user):
    if UserRecordExists(user):
        if DeleteUserRecord(user):
            print("\tRemoved user record from Directory Service")
        else:
            print("\tUnable to remove user record from Directory Service")
    else:
        print("\tUser record does not exist in Directory Service")


if __name__ == "__main__":
    users = GetUsersPlist()
    for user, plist in users.items():
        CheckUserState(user, plist)
