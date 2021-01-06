#!/usr/bin/env python3

import subprocess
import argparse
import sys
import re
import os
import json



def run_shell_command(cmd, quiet=True):
  result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) if quiet else subprocess.run(cmd)
  # if result.returncode != 0:
  #   print("FAILED - {}".format(" ".join(cmd)))
  #   sys.exit(result.returncode)
  return result


def load_triage_data(triage_dbs):
  triage_data = {}
  for json_db in triage_dbs:
    if os.path.exists(json_db):
      with open(json_db) as f:
        db_data = json.load(f)
        triage_data = {**triage_data, **db_data}
  return triage_data


def save_triage_data(triage_data, prev_triage_data, view_only, json_db):
  if not view_only:
    triaged_data = {**prev_triage_data, **triage_data}
    with open(json_db, "w") as f:
      json.dump(triage_data, f)


def display_diff(base_commit, change_commit, filename, i, num_files, default_response):
  os.system("clear")
  print(i + 1, " / ", num_files, "\n")
  if change_commit :
    diff_cmd = ["git", "--no-pager", "diff", base_commit, change_commit, "--", filename]
  else :
    diff_cmd = ["git", "--no-pager", "diff", base_commit, "--", filename]
  diff = run_shell_command(diff_cmd, quiet=False)
  print ("\n"*2)
  response = input("[(i)gnore | (k)eep | (r)efresh | (q)uit ]  :  ").split()
  if len(response) == 0:
    response = default_response
  return response


def is_BAZEL_file(filename):
  match = re.search(r"BUILD$", filename)
  if match:
      return True
  match = re.search(r"WORKSPACE$", filename)
  if match:
      return True
  match = re.search(r"\.bzl$", filename)
  if match:
      return True
  match = re.search(r"\.bazelrc$", filename)
  if match:
      return True
  return False


def is_XLA_file(filename):
  match = re.search(r"^tensorflow/compiler", filename)
  if match:
      return True
  return False


def is_ROCM_FUSION_file(filename):
  match = re.search(r"^tensorflow/core/common_runtime/gpu_fusion*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/core/kernels/gpu_fusion*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/core/kernels/cwise_op_fma*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/core/kernels/cwise_op_gpu_fma*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/python/kernel_tests/gpu_fusion_ops_test*", filename)
  if match:
      return True
  return False


def is_ROCM_DROPOUT_file(filename):
  match = re.search(r"^tensorflow/core/kernels/dropout_op*", filename)
  if match:
      return True
  return False


def is_ROCM_BATCHGEMM_file(filename):
  match = re.search(r"^tensorflow/core/kernels/batch_gemm_op*", filename)
  if match:
      return True
  return False


def is_ROCM_ROCTRACER_file(filename):
  match = re.search(r"^tensorflow/core/profiler/internal/gpu/device_tracer*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/core/profiler/internal/gpu/rocm_tracer*", filename)
  if match:
      return True
  return False


def is_ROCM_DOCS_file(filename):
  match = re.search(r"^rocm_docs/", filename)
  if match:
      return True
  return False


def is_MARKDOWN_file(filename):
  match = re.search(r"\.md$", filename)
  if match:
      return True
  return False


def is_PROTOBUF_file(filename):
  match = re.search(r"\.pbtxt$", filename)
  if match:
      return True
  return False


def is_POOL3D_file(filename):
  match = re.search(r"^tensorflow/python/keras/backend_test*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/python/keras/layers/pooling_test*", filename)
  if match:
      return True
  match = re.search(r"^tensorflow/python/kernel_tests/pool_test*", filename)
  if match:
      return True
  return False


def get_files_of_interest(base_commit, change_commit, prev_triage_data):

  def get_diff_files_list():
    if change_commit :
      diff_cmd = ["git", "diff", "--name-only", base_commit, change_commit]
    else:
      diff_cmd = ["git", "diff", "--name-only", base_commit]
    return run_shell_command(diff_cmd).stdout.decode().split()

  def keep_file(filename):

    if is_XLA_file(filename):
      return False

    if is_ROCM_FUSION_file(filename):
      return False
    
    if is_ROCM_DROPOUT_file(filename):
      return False
    
    if is_ROCM_BATCHGEMM_file(filename):
      return False
    
    if is_ROCM_ROCTRACER_file(filename):
      return False
    
    if is_BAZEL_file(filename):
      return False
    
    if is_ROCM_DOCS_file(filename):
      return False
    
    if is_MARKDOWN_file(filename):
      return False
    
    if is_PROTOBUF_file(filename):
      return False
    
    # if is_POOL3D_file(filename):
    #   return False
    
    # prev_response = prev_triage_data.get(filename, "k").split()[0]
    # if  prev_response != "k":
    #   return False
    
    return True
    
  files_of_interest = []
  for filename in get_diff_files_list():
    if keep_file(filename):
      files_of_interest.append(filename)

  # for f in files_of_interest:
  #   print (f)
    
  return files_of_interest


def triage_diffs(base_commit, change_commit, files_of_interest, default_response):
  num_files = len(files_of_interest)
  triage_data = {}
  for i, filename in enumerate(files_of_interest):
    
    refresh = True
    while refresh:
      response = display_diff(base_commit, change_commit, filename, i, num_files, default_response)
      refresh = response[0] == "r"

    triage_data[filename] = " ".join(response)
    
    if response[0] == "q":
      break

  return triage_data


def main():

  weekly_sync_commit_201116 = "a52c2d085d0ed2fa3f70daf99482fa018cbc0660"
  weekly_sync_commit_201123 = "15f4bda049539dd41c6dd9d0737d33da86cc32cf"
  weekly_sync_commit_201130 = "966694417e2e66c938b3f851fdce661e6aa07f37"
  weekly_sync_commit_201228 = "5688e7ef42c63a0cefbd5ca14c4ebe53e633cd1e"
  
  # ignore_files_db = os.path.join(os.getcwd(), "ignore.json")
  
  base_commit = weekly_sync_commit_201228
  # base_commit = "origin/develop-upstream"

  change_commit = None

  view_only=True
  default_response = ["i"]
  triage_db = os.path.join(os.getcwd(), "build_files.json")
  
  os.chdir("/root/tensorflow")
  prev_triage_data = load_triage_data([triage_db])
  files_of_interest = get_files_of_interest(base_commit, change_commit, prev_triage_data)
  triage_data = triage_diffs(base_commit, change_commit, files_of_interest, default_response)
  save_triage_data(triage_data, prev_triage_data, view_only, triage_db)


if __name__ == '__main__':
  main()
