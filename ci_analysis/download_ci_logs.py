#!/usr/bin/env python3

import requests
import argparse

def get_url(testsuite, run_number):
    ci_job = "develop-upstream-unit-tests"
    testsuite_job = {
        "rocm" : "tensorflow-upstream-unit-tests",
        "rocm-xla" : "tensorflow-upstream-unit-tests-rocm-xla",
        "rocm-cpp" : "tensorflow-upstream-unit-tests-rocm-cpp",
    }
    url = "http://ml-ci.amd.com:21096/job/{}/job/{}/{}/consoleText".format(ci_job, testsuite_job[testsuite], run_number)
    return url


def download_data(userid, password):

    def download_and_save_file(url, filename):
        response = requests.get(url, auth=(userid, password), allow_redirects=True)
        if response.status_code != requests.codes.ok:
            print (response)
            sys.exit(1)
        with open(filename, "w") as f:
            f.write(response.text)

    testsuite = "rocm"
    for run_number in range ():
        download_and_save_file(get_url(testsuite, run_number), local_filename)

if __name__ == '__main__' :

    download_data()
    # process_data()
