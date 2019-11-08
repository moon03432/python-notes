#!/usr/bin/env python3
import datetime
import time

def function():
    print(datetime.datetime.now(), "starting function")
    time.sleep(1)
    print(datetime.datetime.now(), "stoping function")


for i in range(3):
    function()

print(type(time.time()))