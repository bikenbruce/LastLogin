#!python
from plistlib import *
import datetime as dt
import os


def check_password_expired(delete_user=False):
    TODAY = dt.datetime.today()

    for user in os.listdir("/Users"):
        user_home_path = '/Users/' + user
        user_plist = os.path.join(
            user_home_path,
            "Library/Preferences/com.trusourcelabs.NoMAD.plist")
        if os.path.isfile(user_plist):
            # print(user, user_plist)

            try:
                with open(user_plist, 'rb') as fp:
                    pl = load(fp)
                if 'LastPasswordExpireDate' in pl:
                    if pl['LastPasswordExpireDate'] > TODAY:
                        print('user: ' + user + '\texpire date: ' +
                              str(pl['LastPasswordExpireDate'].date()) +
                              '\tstate: not expired')
                    else:
                        print('user: ' + user + '\texpire date: ' +
                              str(pl['LastPasswordExpireDate'].date()) +
                              '\tstate: expired')
                        if delete_user:
                            # remove_user_record(user, user_home_path)
                            pass

            except IOError as err:
                print(err)


if __name__ == "__main__":
    check_password_expired()
