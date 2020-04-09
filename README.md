# NoMAD Client Management Scripts

These are a set of scripts to manage local accounts that are created and maintained with NoMAD.  Att this point in time, these two scripts are intended to be used within a lab environment.

This environment noww includes the python framework folder.  This contains the python executable and libraries that are need to be useed with these scripts.

## lastlogin.py

This script looks at all of the folders that are within the /Users folder on the main hard drive.  With each folder, a last command is run to see when the person last logged into the system.  By default, if the person has not logged into the computer within 30 days, these two acctions will occur:
 
 - Removal of the account record in directory services
 - Create a disk image of the user's folder.  Name of the dmg is the towwer id number, the name of the computer and followed by the last login date.

### goals

Here's a list of goals that would be helpful with this script.

 - Upload dmg files to cha-ds, or some other location

## passwordexpired.py

This script is intended to run on a daily basis.  It looks at the plist information within each user account that contains the date of when the AD password will expire.  If it has expired, the account record will be deleted on the local system.

### goals

- Add this script to run daily upon boot.  Maybe use outset for this?


## Notes

### looking into using

- [outset](https://github.com/chilcote/outset)
- [relocatable python](https://github.com/gregneagle/relocatable-python)
- [launchd info](https://www.launchd.info/)
- [moving to pipenv](https://blog.tecladocode.com/migrating-from-pip-virtualenv-to-pipenv/)

### example code

- [notes from....](https://derflounder.wordpress.com/2016/12/21/migrating-ad-mobile-accounts-to-local-user-accounts/)
