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


def ArchiveHomeFolder(user, home_folder, destination_folder):
    if not os.path.exists(destination_folder):
        exit(1)
    destination = os.path.join(destination_folder, user)
    state = subprocess.run(['/usr/bin/hdiutil', 'create',
                            '-srcfolder', home_folder,
                            '-format', 'ULFO', destination],
                           capture_output=True)
    if state.returncode == 0:
        # now delete home folder.... :)
        return(True)
    else:
        return(False)
