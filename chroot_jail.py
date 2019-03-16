#!/usr/bin/python3
from distutils.dir_util import copy_tree
import os
import sys

#trying to be a root to create dirs under root dir
if os.geteuid() == 0:
        print("We're root!")
else:
    print("We're not root.")
    os.execvp('sudo', ['sudo', 'python3'] + sys.argv)
# detect the current working directory and print it
print (os.getcwd())
#change the current directory to root directory
os.chdir(os.getenv("HOME"))
os.chdir('..')
os.chdir('..')
os.chdir("../mnt")
print (os.getcwd())
#start creating the jail
os.mkdir("new_root")
os.chdir("new_root")
os.chroot("../new_root")
os.mkdir("etc")
os.mkdir("bin")
os.mkdir("bash")
os.mkdir("lib64")
#check jail is working or not
print(os.getcwd())


#copy the files needed it works in other files normally but not in here

fromDirectory = "/bin"
toDirectory = "/mnt/new_root/bin"

copy_tree(fromDirectory, toDirectory)

fromDirectory = "/etc"
toDirectory = "/mnt/new_root/etc"

copy_tree(fromDirectory, toDirectory)

fromDirectory = "/bash"
toDirectory = "/mnt/new_root/bash"

copy_tree(fromDirectory, toDirectory)
#since I can't copy the needed files my script can't run.

file = open('file.sh', 'x')
file.write("#! /bin/bash\r\necho 'Hello World! I am bash script.'\r\n")
file.close()
