#! /usr/bin/python3

import subprocess
import re

cmds = """
./bin/MIOpenDriver convbfp16 -n 64 -c 1 -H 28 -W 28 -k 32 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 1 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 1 -H 28 -W 28 -k 32 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 1 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 32 -H 14 -W 14 -k 64 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 1 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 32 -H 14 -W 14 -k 64 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 1 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 32 -H 14 -W 14 -k 64 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 2 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 32 -H 14 -W 14 -k 64 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 2 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 32 -H 14 -W 14 -k 64 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 4 -t 1
./bin/MIOpenDriver convbfp16 -n 64 -c 1 -H 28 -W 28 -k 32 -y 5 -x 5 -p 2 -q 2 -u 1 -v 1 -l 1 -j 1 -m conv -g 1 -F 4 -t 1
"""

def run_all():
    for i, cmd in enumerate(cmds.split("\n")):
        if cmd :
            driver_cmd = " && ".join(["cd /root/miopen/build", cmd])
            print (driver_cmd)
            driver_output = subprocess.run(driver_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if driver_output.returncode == 0 :
                print ("PASS")
            else :
                print ("FAIL")
            print (driver_output.stdout.decode())


for _ in range(10):
    run_all()

        
