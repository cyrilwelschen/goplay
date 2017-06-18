#!/usr/bin/python3

import subprocess
import os

proc = subprocess.Popen(["pwd"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
current_path_new = str(out, 'utf-8')[:-1]

print("Hello from "+current_path_new)

old_path = "/home/cyril/.bashrc"
temp = "/home/cyril/bashrc_temp"

os.system("mv "+old_path+" "+temp)
os.system("touch "+old_path)

with open(temp, 'r') as in_file, open(old_path, 'w') as out_file:
    for line in in_file:
        if "alias goplay" in line:
            print("Changing alias\n\t"+line)
            new_line = 'alias goplay="cd '+current_path_new+'"\n'
            print("to...\n\t"+new_line)
            out_file.write(new_line)
        else:
            out_file.write(line)

os.system("rm "+temp)

#proc2 = subprocess.Popen(["source", old_path], shell=True)
#os.system("source "+old_path)
