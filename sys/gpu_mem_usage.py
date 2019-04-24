#! /usr/bin/python3

import glob
import time

def get_mem_usage(membanks):
    mem_usage = []
    for mem in membanks:
        with open(mem) as f:
            usage = int(f.read())
            mem_usage.append(usage)
    return mem_usage

def watch_mem_usage():
    find_string="/sys/class/kfd/kfd/topology/nodes/**/used_memory"
    membanks = sorted(glob.glob(find_string, recursive=True))

    print ("Memory bank display order")
    for i,mem in enumerate(membanks):
        print("{} = {}".format(i,mem))

    # header
    for i,mem in enumerate(membanks):
        print("{:^5d}  ".format(i), end="")
    print("")    
    print("-------"*len(membanks))

    # usage
    while True:
        for usage in get_mem_usage(membanks):
            print("{:5.2f}  ".format(usage/(1024*1024)), end="")
        print("")    
        time.sleep(1)

watch_mem_usage()
                       


    
