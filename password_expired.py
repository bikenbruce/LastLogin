from plistlib import *
import datetime as dt
import dateutil.parser as dparser
import os

TODAY = dt.datetime.today()

def check_password_expired():
   for user in os.listdir("/Users"):
      user_plist = os.path.join("/Users", user, "Library/Preferences/com.trusourcelabs.NoMAD.plist")
      if os.path.exists(user_plist):
         print(user_plist)

         try:
            with open(user_plist, 'rb') as fp:
               pl = load(fp)
            if pl['LastPasswordExpireDate'] > TODAY:
               print('not expired')
            else:
               print('expired')

         except:
            print('unable to open file')
            pass

if __name__ == "__main__":
	check_password_expired()
