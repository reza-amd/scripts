#!/home/deven/anaconda3/bin/python3

import os
import subprocess
import filecmp
import shutil

upstream_dir = "/home/deven/deven/projects/eigen_upstream/rocm_fork/eigen-upstream"
official_dir = "/home/deven/deven/projects/eigen_upstream/official_fork/eigen"

def upstream_switch_to_master():
    os.chdir(upstream_dir)
    os.system("git checkout -q master")

def upstream_switch_to_develop():
    os.chdir(upstream_dir)
    os.system("git checkout -q develop-upstream")

def official_switch_to_default():
    os.chdir(official_dir)
    os.system("hg update -q default")
    
def get_changed_files() :

    official_switch_to_default();
    upstream_switch_to_master();
    
    status = 0
    try :
        os.chdir(upstream_dir)
        output = subprocess.check_output("git diff --name-only master develop-upstream".split())
    except subprocess.CalledProcessError as e :
        print("Doh!")
        print(e.output)
        status = 1

    return status, output.decode("utf-8").split()


def diff_file(f) :

    status = 0
    if os.path.isfile(f) :
        f1 = os.path.join(upstream_dir, f)
        f2 = os.path.join(official_dir, f)
        if not filecmp.cmp(f1, f2) :
            print("diff {} {}".format(f1, f2))
            status = 1
    else:
        print ("New File - {}".format(f))
    return status


def verify_files_are_same(changed_files) :

    upstream_switch_to_master();

    status = 0
    for f in changed_files :
        status += diff_file(f)

    return status


def copy_file(f) :
    
    f1 = os.path.join(upstream_dir, f)
    f2 = os.path.join(official_dir, f)

    shutil.copyfile(f1, f2)
    os.system("hg add {}".format(f))
    

def copy_changed_files(changed_files) :

    upstream_switch_to_develop();
    os.chdir(official_dir)

    for f in changed_files :
        copy_file(f)


if __name__ == "__main__" :

    status, changed_files = get_changed_files()
    if status == 0 :
        if verify_files_are_same(changed_files) == 0:
            copy_changed_files(changed_files)

    upstream_switch_to_develop();
    
            
