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
    diff_cmd = ["git", "diff", base_commit, change_commit, "--", filename]
  else :
    diff_cmd = ["git", "diff", base_commit, "--", filename]
  diff = run_shell_command(diff_cmd, quiet=False)
  print ("\n"*2)
  response = input("[(i)gnore | (k)eep | (r)efresh | (d)one ]  :  ").split()
  if len(response) == 0:
    response = default_response
  return response
    

def get_files_of_interest(base_commit, change_commit, prev_triage_data):

  def get_diff_files_list():
    if change_commit :
      diff_cmd = ["git", "diff", "--name-only", base_commit, change_commit]
    else:
      diff_cmd = ["git", "diff", "--name-only", base_commit]
    return run_shell_command(diff_cmd).stdout.decode().split()

  # def skip_file(filename):
  #   prev_response = prev_triage_data.get(filename, "k").split()[0]
  #   return  prev_response == "i"
    
  def skip_file(filename):
    match = re.search(r"BUILD$", filename)
    if match is None:
      return True
    prev_response = prev_triage_data.get(filename, "k").split()[0]
    return  prev_response == "i"
    
  files_of_interest = []
  for filename in get_diff_files_list():
    if not skip_file(filename):
      files_of_interest.append(filename)
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
    
    if response[0] == "d":
      break

  return triage_data


def main():

  weekly_sync_commit_201116 = "a52c2d085d0ed2fa3f70daf99482fa018cbc0660"
  weekly_sync_commit_201123 = "15f4bda049539dd41c6dd9d0737d33da86cc32cf"
  ignore_files_db = os.path.join(os.getcwd(), "ignore.json")
  
  # base_commit = weekly_sync_commit_201123
  # base_commit = "origin/develop-upstream-deven-misc-201123"

  base_commit = "origin/develop-upstream"
  change_commit = None
  view_only=True
  default_response = ["i"]
  triage_db = os.path.join(os.getcwd(), "build_files.json")
  
  os.chdir("/root/tensorflow")
  prev_triage_data = load_triage_data([ignore_files_db, triage_db])
  files_of_interest = get_files_of_interest(base_commit, change_commit, prev_triage_data)
  triage_data = triage_diffs(base_commit, change_commit, files_of_interest, default_response)
  save_triage_data(triage_data, prev_triage_data, view_only, triage_db)


if __name__ == '__main__':
  main()
