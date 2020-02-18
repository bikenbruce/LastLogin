from plistlib import *
import datetime as dt
import dateutil.parser as dparser
import os

TODAY = dt.datetime.today()

def check_password_expired():
   for user in os.listdir("/Users"):
      user_plist = os.path.join("/Users", user, "Library/Preferences/com.trusourcelabs.NoMAD.plist")
      if os.path.isfile(user_plist):
         # print(user, user_plist)

         try:
            with open(user_plist, 'rb') as fp:
               pl = load(fp)
            if 'LastPasswordExpireDate' in pl:
               if pl['LastPasswordExpireDate'] > TODAY:
                  print('user: ' + user + '\texpire date: ' + str(pl['LastPasswordExpireDate'].date()) + '\tstate: not expired')
               else:
                  print('user: ' + user + '\texpire date: ' + str(pl['LastPasswordExpireDate'].date()) + '\tstate: expired')
                  # sysadminctl

         except IOError as err:
            print(err)

if __name__ == "__main__":
	check_password_expired()
