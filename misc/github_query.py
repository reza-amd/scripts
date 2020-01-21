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
   commits(first:20) {\
    edges {\
     node {\
      commit {\
       oid\
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
    print(curl_cmd)
    
    result = subprocess.run(curl_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print ("FAILED - ", curl_cmd)
        return None

    return (result.stdout.decode())

def get_commits_for_pr(owner, name, pr_number):
    query_str = pr_commits_template.substitute(owner=owner, name=name, pr_number=pr_number)
    json_result = run_github_query(query_str)
    result = json.loads(json_result)
    print (result)
    title = result["data"]["repository"]["pullRequest"]["title"]
    commits = [x["node"]["commit"]["oid"] for x in result["data"]["repository"]["pullRequest"]["commits"]["edges"]]
    return (title, commits)

def get_commits_for_google_upstream_pr(pr_number):
    return get_commits_for_pr('\\"tensorflow\\"', '\\"tensorflow\\"', pr_number)

def get_commits_for_rocm_fork_pr(pr_number):
    return get_commits_for_pr('\\"ROCmSoftwarePlatform\\"', '\\"tensorflow-upstream\\"', pr_number)

def print_pr_commits(repo, pr_number, title, commits):
    print('    PRs.append([')
    print('        "{}",'.format(repo))
    print('        "{}",'.format(pr_number))
    print('        "{}",'.format(title))
    print('        [')
    for commit in commits:
        print('            "{}",'.format(commit))
    print('        ]])')
    print('')

def get_google_upstream_PRs():
    PRs = []
    PRs.append(35834)
    PRs.append(35881)
    # PRs.append()
    return PRs
    
def get_rocm_fork_PRs():
    PRs = []
    PRs.append(789)
    PRs.append(790)
    # PRs.append()
    return PRs
    
def generate_pr_commits():
    print ("def get_PRs():")
    print ("    PRs = []")
    print ("")
    
    google_upstream_PRs = get_google_upstream_PRs()
    for pr_number in google_upstream_PRs:
        title, commits = get_commits_for_google_upstream_pr(pr_number)
        print_pr_commits("google_upstream", pr_number, title, commits)
    
    rocm_fork_PRs = get_rocm_fork_PRs()
    for pr_number in rocm_fork_PRs:
        title, commits = get_commits_for_rocm_fork_pr(pr_number)
        print_pr_commits("rocm_fork", pr_number, title, commits)

    print("return PRs")

def simple_query():
    output = run_query("query { viewer { login }}")
    print(output)

if __name__ == "__main__" :
    # simple_query()
    generate_pr_commits()
