#! /usr/bin/python3

import os
import sys
import subprocess

my_env = os.environ.copy()
my_home = my_env["HOME"]
proc = subprocess.Popen('{}/.Scripts/getvolume.sh'.format(my_home), stdout=subprocess.PIPE)
tmp = proc.stdout.read()
a = str(tmp,'utf-8')
b = sys.argv[1]
a = int(a)

proc = subprocess.Popen('{}/.Scripts/getsink.sh'.format(my_home), stdout=subprocess.PIPE)
tmp1 = proc.stdout.read()
z = str(tmp1,'utf-8')
z = int(z)
if (b == "i") and (a != 100 ) :
    os.system("pactl set-sink-volume {} +5%".format(z))
elif b == "d":
	os.system("pactl set-sink-volume {} -5%".format(z))


