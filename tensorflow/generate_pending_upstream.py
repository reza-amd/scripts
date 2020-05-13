#!/usr/bin/env python3

import subprocess
import argparse
import sys
import re

from datetime import date

from openpyxl import Workbook
from openpyxl.styles import NamedStyle


def run_shell_command(cmd):
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print("FAILED - {}".format(" ".join(cmd)))
        print("         {}".format(result.stdout.decode()))
        print("         {}".format(result.stderr.decode()))
        sys.exit(result.returncode)
    return result


def generate_diff_stats(upstream_branch, fork_branch):
    
    result = run_shell_command(["git", "diff", "--numstat", upstream_branch, fork_branch, "--"])
    diff_stats = result.stdout.decode().split('\n')
    diff_stats.pop() # last entry is an empty line

    # for stat in diff_stats:
    #     num_lines_added, num_lines_deleted, filename = stat.split('\t')
    #     print (num_lines_added, num_lines_deleted, filename)

    return diff_stats


def display_diffs(upstream_branch, fork_branch, diff_stats):

    # pattern = r'third_party/'
    # pattern = r'tensorflow/core/grappler/optimizers/'
    # pattern = r'tensorflow/core/profiler/internal/gpu/
    pattern = r'tensorflow/core/common_runtime'
    
    for stat in diff_stats:
        num_lines_added, num_lines_deleted, filename = stat.split('\t')
        match = re.match(pattern, filename)
        if match is not None:
            # subprocess.run(["git", "diff", "--word-diff", upstream_branch, fork_branch, "--", filename])
            subprocess.run(["git", "diff", upstream_branch, fork_branch, "--", filename])
            

def write_to_excel(upstream_branch, fork_branch, diff_stats, excel_file):
    
    workbook = Workbook()
    sheet = workbook.active

    sheet.append(["branch1:", upstream_branch])
    sheet.append(["branch2:", fork_branch])
    sheet.append([])
    sheet.append(["command to display diff for <filename>:", "git diff {} {} -- <filename>".format(upstream_branch, fork_branch)])
    sheet.append([])
    sheet.append(["# lines ADDED", "# lines DELETED", "Filename"])
    for stat in diff_stats:
        sheet.append(stat.split('\t'))

    workbook.save(filename=excel_filename)


if __name__ == '__main__':

    today = date.today()
    excel_filename = "/common/pending_upstream_{}.xlsx".format(today.strftime("%y%m%d"))
    upstream_branch = "origin/master-with-triaged-diffs"
    fork_branch = "origin/develop-upstream-sync-200511"

    # run_shell_command(["git", "fetch", "origin"])
    diff_stats = generate_diff_stats(upstream_branch, fork_branch)

    display_diffs(upstream_branch, fork_branch, diff_stats)
    
    # write_to_excel(upstream_branch, fork_branch, diff_stats, excel_filename)
