import os
import subprocess


def UserRecordExists(home_folder):
    state = subprocess.run(['/usr/bin/dscl', '.', '-read', home_folder],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def UserHomeFolderExists(home_folder):
    if os.path.isdir(home_folder):
        return(True)
    else:
        return(False)


def DeleteUserRecord(home_folder):
    state = subprocess.run(['/usr/bin/dscl', '.', '-delete', home_folder],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def ArchiveHomeFolder(user, destination_folder):
    if not os.path.exists(destination_folder):
        exit(1)
    # Create DMG of home folder
    print('archiving user folder:' + user + 'to:' + destination_folder)

    home_folder = os.path.join('/Users', user)
    destination = os.path.join(destination_folder, user)
    state = subprocess.run(['/usr/bin/hdiutil', 'create',
                            '-srcfolder', home_folder,
                            '-format', 'ULFO', destination],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)
        break()


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
        break()
