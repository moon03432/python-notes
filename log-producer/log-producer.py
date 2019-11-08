#!/usr/bin/env python3
import datetime
import sys

current_time = datetime.datetime.now();
day = current_time.strftime('%Y-%m-%d');
time = current_time.strftime('%Y-%m-%d.%H:%M:%S');

f = open(sys.argv[1]+'/'+day+".log", 'a')
f.write( time + " logging\n")
f.close()

