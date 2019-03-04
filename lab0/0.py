#!/usr/bin/env python
import os
import time

os.chdir(os.getenv("HOME"))
os.mkdir("os_lab_0")
os.chdir("os_lab_0")
os.system("touch a.txt b.txt c.py")
#print time.ctime(max(os.path.getmtime(root) for root,_,_ in os.walk('../os_lab_0')))
print (os.system("ls -l"))
for file in os.listdir("../os_lab_0"):

    if file.endswith(".txt"):
            print(os.path.join(file))
