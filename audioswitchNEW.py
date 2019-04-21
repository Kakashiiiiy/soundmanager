#! /usr/bin/python3
import subprocess
import os
from shlex import split

my_env = os.environ.copy()
my_home = my_env["HOME"]
proc = subprocess.Popen( '{}/.Scripts/getvolume.sh'.format(my_home), stdout=subprocess.PIPE,env=my_env)
tmp = proc.stdout.read()
volume_a_sink = int(str(tmp,'utf-8'))

proc = subprocess.Popen('{}/.Scripts/getsink.sh'.format(my_home), stdout=subprocess.PIPE)
tmp = proc.stdout.read()
activesink = int(str(tmp,'utf-8'))

proc = subprocess.Popen('{}/.Scripts/listallsinks.sh'.format(my_home), stdout=subprocess.PIPE)
tmp = proc.stdout.read()
tmp1 = (str(tmp,'utf-8'))
tmp2 = tmp1.split('\n')[:-1]

allsinks = [0]* (len(tmp2))
for i in range(len(tmp2)):
	allsinks[i] = int(tmp2[i])

for i in range(len(tmp2)):
	if activesink == allsinks[i]:
		try:
			nextsink = allsinks[i+1]
		except IndexError:
			nextsink = allsinks[0]
		comm1 = "pactl set-sink-volume {} {}%".format(nextsink,volume_a_sink)
		comm2 = "pacmd set-default-sink {}".format(nextsink)
		comm3 = "pacmd set-default-source {}".format(nextsink)


proc = subprocess.Popen(split(comm1), stdout=subprocess.PIPE)
proc = subprocess.Popen(split(comm2), stdout=subprocess.PIPE)
proc = subprocess.Popen(split(comm3), stdout=subprocess.PIPE)

proc = subprocess.Popen('{}/.Scripts/activeaudioprogs.sh'.format(my_home), stdout=subprocess.PIPE)
tmp = proc.stdout.read()
tmp1 = (str(tmp,'utf-8'))
tmp2 = tmp1.split('\n')[:-1]

tmp3 = [0]* (len(tmp2))
for i in range(len(tmp2)):
	tmp3[i] = int(tmp2[i])

proc = subprocess.Popen('{}/.Scripts/defaultsinkname.sh'.format(my_home), stdout=subprocess.PIPE)
tmp = proc.stdout.read()
sinkname = (str(tmp,'utf-8'))
for i in tmp3:
	comm4 = "pacmd move-sink-input {} {}".format(i,sinkname)
	proc = subprocess.Popen(split(comm4), stdout=subprocess.PIPE)
subprocess.run(["pkill", "-RTMIN+2",  "waybar"])
