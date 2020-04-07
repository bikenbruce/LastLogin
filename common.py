import os
import subprocess


def UserRecordExists(user):
    home_folder = os.path.join('/Users', user)
    state = subprocess.run(['/usr/bin/dscl', '.', '-read', home_folder],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def UserHomeFolderExists(user):
    if os.path.isdir(os.path.join('/Users', user)):
        return(True)
    else:
        return(False)


def DeleteUserRecord(user):
    home_folder = os.path.join('/Users', user)
    state = subprocess.run(['/usr/bin/dscl', '.', '-delete', home_folder],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def ArchiveHomeFolder(user, destination_folder, note=None):
    if not os.path.exists(destination_folder):
        exit(1)

    home_folder = os.path.join('/Users', user)
    if note is None:
        destination = os.path.join(destination_folder, user)
    else:
        destination = os.path.join(destination_folder, user) + "-" + note
    state = subprocess.run(['/usr/bin/hdiutil', 'create',
                            '-srcfolder', home_folder,
                            '-format', 'ULFO', destination])
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def DeleteHomeFolder(user):
    home_folder = os.path.join('/Users', user)
    if not os.path.exists(home_folder):
        exit(1)
    
    state = subprocess.run(['/bin/rm', '-rf', home_folder],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)
