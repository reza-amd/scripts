#! /usr/bin/python3

import subprocess
import json
from string import Template


# prs_template = Template("""\
# query {\
#  repository(owner:$owner, name:$name) {\
#   pullRequests(first:10) {\
#    edges {\
#     node {\
#      title\
#     }\
#    }\
#   }\
#  }\
# }\
# """)


pr_commits_template = Template("""\
query {\
 repository(owner:$owner, name:$name) {\
  pullRequest(number:$pr_number) {\
   title\
   state\
   commits(first:20) {\
    edges {\
     node {\
      commit {\
       oid\
       parents {\
        totalCount\
       }\
      }\
     }\
    }\
   }\
  }\
 }\
}\
""")


def get_token():
    with open("/common/git_token.txt") as f:
        token = f.read()
        return token.strip()
    return None

def run_github_query(query):

    curl_cmd = ["curl"]

    auth_string = 'Authorization: Bearer {}'.format(get_token())
    curl_cmd.extend(["-H", auth_string])
    
    query_string = '{{ "query" : "{}" }}'.format(query)
    curl_cmd.extend(["-d", query_string])

    curl_cmd.extend(["-X", "POST"])
    curl_cmd.extend(["https://api.github.com/graphql"])

    # print(query_string)
    # print(curl_cmd)
    
    result = subprocess.run(curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print ("FAILED - ", curl_cmd)
        return None

    return (result.stdout.decode())

def get_commits_for_pr(owner, name, pr_number):
    query_str = pr_commits_template.substitute(owner=owner, name=name, pr_number=pr_number)
    json_result = run_github_query(query_str)
    result = json.loads(json_result)
    # print (result)
    pullRequest = result["data"]["repository"]["pullRequest"]
    title = pullRequest["title"]
    state = pullRequest["state"]
    commits = [x["node"]["commit"] for x in pullRequest["commits"]["edges"]]
    return (title, state, commits)

def get_commits_for_google_upstream_pr(pr_number):
    return get_commits_for_pr('\\"tensorflow\\"', '\\"tensorflow\\"', pr_number)

def get_commits_for_rocm_fork_pr(pr_number):
    return get_commits_for_pr('\\"ROCmSoftwarePlatform\\"', '\\"tensorflow-upstream\\"', pr_number)

def print_pr_commits(repo, pr_number, title, state, commits):

    # print ('{} - {} : {}'.format(state, pr_number, title))

    if (state != "OPEN"):
        return

    print ('    PRs.append([')
    print ('        "{}",'.format(repo))
    print ('        "{}",'.format(pr_number))
    print ('        "{}",'.format(title))
    print ('        [')
    for commit in commits:
        oid = commit["oid"]
        num_parents = commit["parents"]["totalCount"]
        if num_parents > 1 :
            print ('            # "{}",'.format(oid))
        else :
            print ('            "{}",'.format(oid))
    print ('        ]])')
    print ('')

def get_google_upstream_PRs():
    PRs = []
    PRs.append(35394)
    PRs.append(35395)
    PRs.append(35519)
    PRs.append(35624)
    PRs.append(35666)
    PRs.append(35752)
    PRs.append(35890)
    PRs.append(35891)
    PRs.append(35924)
    PRs.append(35964)
    PRs.append(35965)
    PRs.append(35966)
    PRs.append(35971)
    PRs.append(35972)
    PRs.append(35991)
    PRs.append(36017)
    PRs.append(36018)
    PRs.append(36019)
    PRs.append(36031)
    PRs.append(36032)
    PRs.append(36106)
    PRs.append(36110)
    PRs.append(36187)
    PRs.append(36191)
    return PRs
    
def get_rocm_fork_PRs():
    PRs = []
    PRs.append(782)
    PRs.append(783)
    PRs.append(789)
    PRs.append(790)
    PRs.append(791)
    PRs.append(794)
    PRs.append(795)
    PRs.append(799)
    PRs.append(803)
    # PRs.append()
    return PRs
    
def generate_pr_commits():
    print ("def get_PRs():")
    print ("    PRs = []")
    print ("")
    
    google_upstream_PRs = get_google_upstream_PRs()
    for pr_number in google_upstream_PRs:
        title, state, commits = get_commits_for_google_upstream_pr(pr_number)
        print_pr_commits("google_upstream", pr_number, title, state, commits)
    
    rocm_fork_PRs = get_rocm_fork_PRs()
    for pr_number in rocm_fork_PRs:
        title, state, commits = get_commits_for_rocm_fork_pr(pr_number)
        print_pr_commits("rocm_fork", pr_number, title, state, commits)

    print ("    return PRs")

def simple_query():
    output = run_query("query { viewer { login }}")
    print(output)

if __name__ == "__main__" :
    # simple_query()
    generate_pr_commits()
