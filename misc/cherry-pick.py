#! /usr/bin/python3

import subprocess
import argparse
from pr_database import get_PRs


def check_for_merge_commit(commits):

    commits_from_this_PR = set();
    head_commit = None
    base_commit = None
    has_merge_commit = False
    
    for commit, parents in commits:
        head_commit = commit
        commits_from_this_PR.add(commit)
        if len(parents) > 1:
            has_merge_commit = True
        for parent in parents:
            if parent not in commits_from_this_PR:
                base_commit = parent

    return has_merge_commit, base_commit, head_commit
    

def cherry_pick_simple(number, title, commits):

    for commit, parents in commits:
        cherry_pick_cmd = ["git", "cherry-pick", "--no-commit", commit]
        # print (cherry_pick_cmd)
        result = subprocess.run(cherry_pick_cmd)
        if result.returncode != 0:
            print ("...FAILED (cherry-pick --no-commit)")
            return result.returncode

    commit_cmd = ["git", "commit", "-m", "PR {} - {}".format(number, title)]
    result = subprocess.run(commit_cmd)
    if result.returncode != 0:
        print ("...FAILED (commit)")
        return result.returncode

    return result.returncode


def cherry_pick_diff_apply(number, title, base_commit, head_commit):

    diff_cmd = ["git", "diff", "{}...{}".format(base_commit, head_commit), "--color=never", "--output", "patch.diff"]
    result = subprocess.run(diff_cmd)
    if result.returncode != 0:
        print ("...FAILED (diff)")
        return result.returncode

    apply_cmd = ["git", "apply", "--whitespace=nowarn", "patch.diff"]
    result = subprocess.run(apply_cmd)
    if result.returncode != 0:
        print ("...FAILED (apply)")
        return result.returncode
        
    commit_cmd = ["git", "commit", "--all", "-m", "PR {} - {}".format(number, title)]
    result = subprocess.run(commit_cmd)
    if result.returncode != 0:
        print ("...FAILED (commit)")
        return result.returncode

    return result.returncode


def cherry_pick_PRs(args):

    dest_branch_base_commit = args.base_commit

    for repo, number, title, state, pr_merge_commit, commits in get_PRs():

        if (repo == "rocm_fork") and (not args.merge_rocm_prs) :
            continue

        print ("")
        print ("Cherry-picking {} PR {} - {}".format(state, number, title), end="")

        if state == "CLOSED":
            print ("...Skipping cherry pick as PR was CLOSED without merging")
            continue
            
        if state == "MERGED":
            assert (pr_merge_commit != "None")
            is_ancestor_cmd = ["git", "merge-base", "--is-ancestor", pr_merge_commit, dest_branch_base_commit]
            # print (is_ancestor_cmd)
            result = subprocess.run(is_ancestor_cmd)
            if result.returncode == 0:
                print ("...Skipping cherry pick as PR is ALREADY MERGED into the destination branch")
                continue

        has_merge_commit, base_commit, head_commit = check_for_merge_commit(commits)
        if (repo == "google_upstream") and has_merge_commit:
            print ("...using the DIFF_APPLY route to do the cherry-picking")
            result = cherry_pick_diff_apply(number, title, base_commit, head_commit)
            if result != 0:
                return
        else:
            print ("...using the SIMPLE route to do the cherry-picking")
            result = cherry_pick_simple(number, title, commits)
            if result != 0:
                return

            
            
def cherry_pick_commits():

    commits = [
        "2294526571ca2bb959a616b3feceebef8e525b7c",
        "916584b2746064ba3096200c4129a56320124b1c",
        "72bae743a5a6d1ec03078b494df37f8c2ddd2b08",
        "900a3db2a5af1992dc5d771edbb0874afd5a3ad3",
        "236cb3ac9fc40567b0f2ac6d8752cdbd523735f2",
        "8e1987c2db551ad44cbb60f292bb89d8fe37f1dd",
        "7387909d1cf10143ef0e33e8fc4652846297ec0a",
        "8fc5646d0ce97fbef44727dcf36c1c9a6a672ee9",
        "67f97220a9a3be65fb4e7cddf6d32afdadb2297e",
        "80f8bb77c698f1bae573dcdb3329b2e4d8cd815c",
        ]


    for commit in commits:
        cherry_pick_cmd = ["git", "cherry-pick", commit]
        result = subprocess.run(cherry_pick_cmd)
        if result.returncode != 0:
            print ("...FAILED (cherry-pick {}".format(commit))
            return

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_commit")
    parser.add_argument("--merge_rocm_prs", action='store_true')
    args = parser.parse_args()

    if not args.base_commit :
        result = subprocess.run(["git", "rev-parse", "HEAD"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print('ERROR...call to "git rev-parse HEAD" failed.')
            print('\t', result.stderr.decode())
            return
        args.base_commit = result.stdout.decode()
    
    cherry_pick_PRs(args)
    
if __name__ == "__main__" :
    main()
    
