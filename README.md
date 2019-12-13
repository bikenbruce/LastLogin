# last_login.py
A simple script at this point, that looks at each of the folders within the /Users directory and looks for a last login of that user.  I've had to do some text parsing to filter down the results from the `last` command.

# goals
- list users that have not logged in after _x_ number of days.
- remove users that have not logged in after _x_ number of days.
- create application via py2app to bundle python with the script so it is compatable with mac os catalia and forward.

# requirements
- python3
- virtualenv
- required python modules are listed in requirements.txt

# installation
- brew.  Look to https://brew.sh for installation.
- python3: installed `brew install python3`
- virtualenv: installed via `pip3 install virtualenv`
- Modules: installed via `virtualenv venv -r requirements.txt`

# running
here's a sample output:

```
$ python last_login.py -h

usage: last_login.py [-h] [-d DAYS]

show duration since last login for each user

optional arguments:
  -h, --help            show this help message and exit
  -d DAYS, --days DAYS  number of days since last log in (defult: 30)

$ python last_login.py 
user: bruce 	last_log:  Fri Dec 13 13:39 	last_log_time: 2019-12-13 13:39:00
```

