# last_login.py

A simple script at this point, that looks at each of the folders within the /Users directory and looks for a last login of that user.  If the login time is greater than 30 days, a message will appear to indicate so.

## goals

- list users that have not logged in after _x_ number of days.
- remove users that have not logged in after _x_ number of days.
- create application via py2app to bundle python with the script so it is compatable with mac os catalia and forward.

## requirements

- python3
- virtualenv
- required python modules are listed in requirements.txt

## installation

- brew.  Look to <https://brew.sh> for installation.
- python3: installed `brew install python3`
- virtualenv: installed via `pip3 install virtualenv`, followed by `virtualenv venv -p python3`
- Modules: installed via `virtualenv venv -r requirements.txt`

## running

here's a sample output:

```zsh
$ python last_login.py -h

usage: last_login.py [-h] [-d DAYS]

show duration since last login for each user

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --days DAYS  number of days since last log in (defult: 30)

$ python last_login.py 
user: bruce 	last_log:  Fri Dec 13 13:39 	last_log_time: 2019-12-13 13:39:00
```

## Notes

### looking into using

- [outset](https://github.com/chilcote/outset)
- [relocatable python](https://github.com/gregneagle/relocatable-python)

### example code

- [notes from....](https://derflounder.wordpress.com/2016/12/21/migrating-ad-mobile-accounts-to-local-user-accounts/)
