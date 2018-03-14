import os, glob, sys
from time import sleep

directory = sys.argv[1]
sleep_time = int(sys.argv[2])
files = None

os.chdir(directory)
files = os.listdir()

while (True):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            cmd = "feh --bg-fill " + file
            os.system(cmd)
            sleep(sleep_time)
