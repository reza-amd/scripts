#!/usr/bin/env python3

import re
import json
import requests
import argparse

def strip_vt100_escape_codes(line):
    # https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python/33925425
    ansi_escape_pattern = r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])'
    return re.sub(ansi_escape_pattern, '', line)


def get_testname_status(line):

    # PASSED_pattern = r'(^[^\s]+)\s+(PASSED) in'
    # match = re.search(PASSED_pattern, line)
    # if match:
    #     return (match.group(1), match.group(2))

    FLAKY_pattern = r'(^[^\s]+)\s+(FLAKY), failed in'
    match = re.search(FLAKY_pattern, line)
    if match:
        print(line)
        return (match.group(1), match.group(2))

    TIMEOUT_pattern = r'(^[^\s]+)\s+(TIMEOUT) in'
    match = re.search(TIMEOUT_pattern, line)
    if match:
        print(line)
        return (match.group(1), match.group(2))
        
    FAILED_pattern = r'(^[^\s]+)\s+(FAILED) in'
    match = re.search(FAILED_pattern, line)
    if match:
        print(line)
        return (match.group(1), match.group(2))
        
    return "", ""


def process_ci_log(ci_log):
    test_status = []
    with open(ci_log) as f:
        for line in f.readlines():
            line = line.strip()
            line = strip_vt100_escape_codes(line)
            testname, status = get_testname_status(line)
            if testname:
                test_status.append([testname, status, line])
    return test_status
    

def write_db(db_file, db_data):
    with open(db_file, "w") as f:
        json.dump(db_data, f)
    

def process_data():

    ci_logs = [
        "/home/deven/Downloads/consoleText_2055",
        "/home/deven/Downloads/consoleText_2095",
    ]
    
    testsuite = "rocm"
    all_results = []
    for ci_log in ci_logs:
        test_results = process_ci_log(ci_log)
        
        ci_run_data = {}
        ci_run_data["testuite"] = testsuite
        ci_run_data["logfile"] = ci_log
        ci_run_data["test_results"] = test_results
        
        all_results.append(test_results)

    db_file = "rocm_test_results.json"
    write_db(db_file, all_results)


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
