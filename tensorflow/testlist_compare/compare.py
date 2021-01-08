#!/usr/bin/env python3

import re


logfiles = {
  # "rocm_cpp" : "set_1/consoleText_cpp",
  # "rocm_xla" : "set_1/consoleText_xla",
  # "rocm_py"  : "set_1/consoleText_py",
  # "rocm_cpu" : "set_1/consoleText_cpu",
  # "rocm_gpu_single" : "set_1/consoleText_gpu_single",
  
  # "rocm_cpp" : "set_2/consoleText_rocm_cpp",
  # "rocm_xla" : "set_2/consoleText_rocm_xla",
  # "rocm_py"  : "set_2/consoleText_rocm_py",
  # "rocm_cpu" : "set_2/consoleText_ubuntu_cpu",
  # "rocm_gpu_single" : "set_2/consoleText_ubuntu_gpu_single",
  # "rocm_gpu_multi" : "set_2/consoleText_ubuntu_gpu_multi",
  # "tf_gpu"   : "set_2/upstream_ubuntu_gpu",


  "rocm_gpu_single" : "set_3/consoleText_ubuntu_gpu_single_93",
  "rocm_gpu_multi" : "set_3/consoleText_ubuntu_gpu_multi_95",
  "tf_gpu"   : "set_3/upstream_ubuntu_gpu_210108",
}


def get_test_list(logfile):
  passed, flaky, failed = [], [], []
  with open(logfile) as f:
    for line in f.readlines():
      if re.search("PASSED in", line):
        passed.append(line.split()[0])
      if re.search("FAILED in", line):
        failed.append(line.split()[0])
      if re.search("FLAKY, ", line):
        flaky.append(line.split()[0])
  return passed, flaky, failed


def print_summary(names):
  print ("-"*100)
  for name in names:
    logfile = logfiles[name]
    passed, flaky, failed = get_test_list(logfile)
    print ("{:20s} - PASSED : {:5d}, FLAKY : {:5d}, FAILED : {:5d}".format(name, len(passed), len(flaky), len(failed)))
  print ("-"*100)


def get_combined_test_list(ci_jobs):
  all_tests = set()
  for ci_job in ci_jobs:
    passed, flaky, failed = get_test_list(logfiles[ci_job])
    all_tests.update(passed)
    all_tests.update(flaky)
    all_tests.update(failed)
  return all_tests
  

def compare_test_lists():
  legacy_ci_jobs = ["rocm_cpp", "rocm_xla", "rocm_py"]
  legacy_test_list = get_combined_test_list(legacy_ci_jobs)
  print ("Number of tests in legacy CI jobs   : ", len(legacy_test_list))
         
  new_ci_jobs = ["rocm_cpu", "rocm_gpu_single", "rocm_gpu_multi"]
  new_test_list = get_combined_test_list(new_ci_jobs)
  print ("Number of tests in new CI jobs      : ", len(new_test_list))

  tests_exclusive_to_legacy = legacy_test_list.difference(new_test_list)
  tests_exclusive_to_new = new_test_list.difference(legacy_test_list)
  tests_common = legacy_test_list.intersection(new_test_list)

  print ("Number of common tests              : ", len(tests_common))
  print ("Number of tests exclusive to legacy : ", len(tests_exclusive_to_legacy))
  print ("Number of tests exclusive to new    : ", len(tests_exclusive_to_new))

  print ("\n\nTests exclusive to legacy\n")
  print ("\n".join(tests_exclusive_to_legacy))

  print ("\n\nTests exclusive to new\n")
  print ("\n".join(tests_exclusive_to_new))


def compare_gpu_lists():
  tf_gpu_list = get_combined_test_list(["tf_gpu"])
  print ("Number of tests in TF GPU job     : ", len(tf_gpu_list))
         
  rocm_gpu_list = get_combined_test_list(["rocm_gpu_single", "rocm_gpu_multi"])
  print ("Number of tests in ROCm GPU job   : ", len(rocm_gpu_list))

  tests_exclusive_to_tf = tf_gpu_list.difference(rocm_gpu_list)
  tests_exclusive_to_rocm = rocm_gpu_list.difference(tf_gpu_list)
  tests_common = tf_gpu_list.intersection(rocm_gpu_list)

  print ("Number of common tests            : ", len(tests_common))
  print ("Number of tests exclusive to TF   : ", len(tests_exclusive_to_tf))
  print ("Number of tests exclusive to ROCm : ", len(tests_exclusive_to_rocm))

  print ("\n\nTests exclusive to TF\n")
  print ("\n".join(sorted(tests_exclusive_to_tf)))

  print ("\n\nTests exclusive to ROCm\n")
  print ("\n".join(sorted(tests_exclusive_to_rocm)))



def main():
  
  # print_summary(["rocm_py", "rocm_cpp", "rocm_xla"])
  # print_summary(["rocm_cpu", "rocm_gpu_single", "rocm_gpu_multi"])
  # compare_test_lists()

  print_summary(["tf_gpu", "rocm_gpu_single", "rocm_gpu_multi"])
  compare_gpu_lists()

if __name__ == '__main__':
  main()
