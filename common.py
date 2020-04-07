import os
import subprocess


def UserRecordExists(path):
    state = subprocess.run(['/usr/bin/dscl', '.', '-read', path],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def UserHomeFolder(path):
    if os.path.isdir(path):
        return(True)
    else:
        return(False)


def DeleteUserRecord(path):
    state = subprocess.run(['/usr/bin/dscl', '.', '-delete', path],
                           capture_output=True)
    if state.returncode == 0:
        return(True)
    else:
        return(False)


def ArchiveHomeFolder(user, path, destination_folder):
    if not os.path.exists(destination_folder):
        exit(1)
    destination = os.path.join(destination_folder, user)
    state = subprocess.run(['/usr/bin/hdiutil', 'create',
                            '-srcfolder', path,
                            '-format', 'ULFO', destination],
                           capture_output=True)
    if state.returncode == 0:
        # now delete home folder.... :)
        return(True)
    else:
        return(False)
