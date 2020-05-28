#! /usr/bin/env python3

import subprocess
import argparse
import sys
import re

from datetime import date

def run_shell_command(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("FAILED - {}".format(" ".join(cmd)))
        print("         {}".format(result.stdout.decode()))
        print("         {}".format(result.stderr.decode()))
        sys.exit(result.returncode)
    return result


def get_xla_tests():
    xla_tests = 'tests(//tensorflow/compiler/...)'
    excluded_tests = 'attr(tags, "no_oss|oss_serial|no_gpu|benchmark-test|v1only", {})'.format(xla_tests)
    xla_ci_tests = '{} except {}'.format(xla_tests, excluded_tests)
    failing_xla_tests = 'attr(tags, no_rocm, {})'.format(xla_ci_tests)
    passing_xla_tests = '{} except {}'.format(xla_ci_tests, failing_xla_tests)

    def get_test_list(query):
        bazel_cmd = ["bazel", "cquery", query]
        result = run_shell_command(bazel_cmd)
        test_list = []
        for line in result.stdout.decode().split('\n'):
            if line:
                testname = line.split()[0]
                test_list.append(testname)
        return test_list

    passing_tests = get_test_list(passing_xla_tests)
    failing_tests = get_test_list(failing_xla_tests)
    return (passing_tests, failing_tests)



def get_cpp_tests():

    cpp_tests = 'kind(cc_*, tests(//tensorflow/... except //tensorflow/compiler/... except //tensorflow/lite/...))'
    excluded_tests = 'attr(tags, "no_oss|oss_serial|no_gpu|benchmark-test|v1only", {})'.format(cpp_tests)
    cpp_ci_tests = '{} except {}'.format(cpp_tests, excluded_tests)
    failing_cpp_tests = 'attr(tags, no_rocm, {})'.format(cpp_ci_tests)
    passing_cpp_tests = '{} except {}'.format(cpp_ci_tests, failing_cpp_tests)

    def get_test_list(query):
        bazel_cmd = ["bazel", "query", query]
        result = run_shell_command(bazel_cmd)
        test_list = []
        for line in result.stdout.decode().split('\n'):
            if line:
                testname = line.strip()
                test_list.append(testname)
        return test_list

    passing_tests = get_test_list(passing_cpp_tests)
    failing_tests = get_test_list(failing_cpp_tests)
    return (passing_tests, failing_tests)



def get_py_tests():

    py_tests = 'kind(py_*, tests(//tensorflow/... except //tensorflow/compiler/... except //tensorflow/lite/...))'
    excluded_tests = 'attr(tags, "no_oss|oss_serial|no_gpu|benchmark-test|v1only", {})'.format(py_tests)
    py_ci_tests = '{} except {}'.format(py_tests, excluded_tests)
    failing_py_tests = 'attr(tags, no_rocm, {})'.format(py_ci_tests)
    passing_py_tests = '{} except {}'.format(py_ci_tests, failing_py_tests)

    def get_test_list(query):
        bazel_cmd = ["bazel", "query", query]
        result = run_shell_command(bazel_cmd)
        test_list = []
        for line in result.stdout.decode().split('\n'):
            if line:
                testname = line.strip()
                test_list.append(testname)
        return test_list

    passing_tests = get_test_list(passing_py_tests)
    failing_tests = get_test_list(failing_py_tests)
    return (passing_tests, failing_tests)



if __name__ == '__main__':

    xla_pass, xla_fail = get_xla_tests()
    cpp_pass, cpp_fail = get_cpp_tests()
    py_pass, py_fail = get_py_tests()

