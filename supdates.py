#!/usr/bin/env python3

"""
This script runs depending on the cron job configuration and will be persistent to a degree in order to maintain and
keep packages updated as best as it can. This script will not provide feedback unless running into an odd error or
asking for better permissions to complete the task. In the case of required elevated permissions a separate popup will
appear to alert the user that they will soon be prompted for their credentials to finish the update on their machine
and that this is not malware and to contact the system administrator for any questions, ie the computer wiz that setup
this machine.
"""

import os
import time
import sys

tmp = 'tmp_packages.txt'
apt_list = '/tmp/apt_list.txt'
packages_to_update = []
ten_packages = []
# os.system(f'apt list --upgradeable > {apt_list}')

with open(tmp, 'r') as package_list:
    package_list.readline()
    for package in package_list.readlines():
        pkg = package.replace('\n', '')
        name, ver = pkg.split('/')
        packages_to_update.append(name)


def update():

    if len(packages_to_update) > 0:
        try:
            for x in range(10):
                ten_packages.append(packages_to_update)
        except IndexError:
            for x in range(len(packages_to_update)):
                ten_packages.append(packages_to_update)

        try:
            os.system(f"apt install -y " + " ".join(ten_packages))
            ten_packages.clear()
        except PermissionError:
            print("[-] Permissions Error")
            # I need to use pyqt to create a popup to tell the user the automated update has failed
            sys.exit(0)
        except ConnectionError:
            print("[-] Connection Error")
            time.sleep(7200)
            update()

        time.sleep(7200)
        update()
    else:
        print("UPDATE FINISHED")


update()
