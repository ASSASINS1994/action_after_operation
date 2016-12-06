#!/usr/bin/python3

import psutil
import os
#here comment

while True:
    iowait = psutil.cpu_times_percent(interval=10).iowait
    print(iowait)
    if iowait < 2:
        os.system("poweroff")
