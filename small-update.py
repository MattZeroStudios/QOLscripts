#!/usr/bin/env python3
import os
import time

file = "/tmp/apt_update_list.txt"
update = os.system('apt update')
command = os.system(f'apt list --upgradable > {file}')
package_to_update = []
package_list = []
package_information = {}
line_count = 0

with open(file) as apt_list:
    # skip past the listing... nonsense
    apt_list.readline()
    for pkg in apt_list.readlines():
        line_count += 1
        strip = pkg.replace('\n', '')
        package = strip.split('/')
        package_information[package[0]] = package[1]
        package_list.append(package)

if line_count > 15:
    try:
        try:
            for x in range(0, 10):
                package_to_update.append(package_list[x][0])
        except IndexError:
            print("[-] Index Error!")

        print("[+] Following packages will be updated " + " ".join(package_to_update))
        time.sleep(2)
        os.system(f"apt install -y " + " ".join(package_to_update))
    except PermissionError:
        print("[-] Please run as root or check if apt is already running elsewhere.")
else:
    try:
        os.system("apt upgrade")
    except PermissionError:
        print("[-] Please run as root or check if apt is already running elsewhere.")
