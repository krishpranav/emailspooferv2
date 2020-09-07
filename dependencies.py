#!usr/bin/env/python

import os
import time

os.system("clear")
print("INSTALLING")
os.system("clear")
print("UPDATING")
os.system("sudo apt-get install update")
os.system("clear")
print("INSTALLING PYTHON")
os.system("sudo apt-get install python3-pip")
os.system("clear")
print("INSTALLING PIP MODULES")
os.system("pip3 install colorama==0.3.9")
os.system("clear")
time.sleep(1)
print("INSTALLATION COMPLETED")
