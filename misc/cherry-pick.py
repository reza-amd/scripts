#! /usr/bin/python3

import subprocess


def get_PRs():
    PRs = []

    # PRs.append([
    #     "google_upstream",
    #     "34800",
    #     "[ROCm] Add ROCm support for CSR Sparse Matrix Ops",
    #     [
    #         "9e7eae9f71855efe83287977e1844806675adaee",
    #         "f725b464549eab744148ad940e04060cbaa7ae90",
    #         "5ad7620d6f18f4a3c123fb7f365f0cb20dda2760",
    #         "7e8ccbd22be53cade35de31631a8ada0bccfbac5",
    #         "2e1cdaa4b62103d1d6f2e18845bbc2c69ffc117b",
    #         "e762347e79f10f0ee3a730385f4959808ec2fb1e",
    #         "5d1ccc1eeeebd527427ff02c24b7a967861e2868",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35360",
    #     "[ROCm] Fix for the broken ROCm CSB - 191223",
    #     [
    #         "e8360cd9b2d10ffb706ebecb5202b77dac84e0cc"
    #     ]])
    
    # PRs.append([
    #     "google_upstream",
    #     "35497",
    #     "[ROCm] Updating Dockerfile.rocm to use ROCm 3.0",
    #     [
    #         "68f7d55e5296626c202fcb57824c0c49af04c8d8"
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35503",
    #     "[ROCm] Updating ROCm implementation to use MIOpen Immediate Mode API",
    #     [
    #         "1ad0ff755e2dddcc37d9b57e271642fd4d1d405d",
    #         "f5b5f3d22dfea28cd62566ed7de67d5bc4640309",
    #         "80c49615ee4501c40efa0b5e2036c73dd1f1e65e",
    #         "81ab633a4934c3e1f673e0abbfb229d7f3c1d029",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35400",
    #     "[ROCm] disabling 3D pooling ops subtests of //tensorflow/cc:gradients_nn_grad_test",
    #     [
    #         "1b1c46ebe85cb0cb0b182c87d896d6499a13b581",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35519",
    #     "[ROCm] Unit-test updates for the ROCm platform",
    #     [
    #         # commit before rebase: "c9f00e8015ea7f8e85ff13c4c3223cd7edfacd92",
    #         "7227ed89ce55d5f760d4a435da2d1fc99701f236",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35401",
    #     "[ROCm] Improved launch config calculation",
    #     [
    #         "8a4be4e58557663cebddc87aae96944515046051",
    #     ]])
    
    # PRs.append([
    #     "google_upstream",
    #     "35572",
    #     "[ROCm] Fix for the broken ROCm CSB - 200103",
    #     [
    #         "ab527339f66193b4c22b10f95165c204ce459f11",
    #         "614babf5f56029ba8b173939ced0447b5f34b9fa",
    #     ]])

    # PRs.append([
    #     "",
    #     "",
    #     "",
    #     [
    #     ]])
    
    return PRs


def cherry_pick_PRs():

    for repo, number, title, commits in get_PRs():
        
        print ("Cherry-picking PR {} - {}".format(number, title))
        
        for commit in commits:
            cherry_pick_cmd = ["git", "cherry-pick", "--no-commit", commit]
            # print (cherry_pick_cmd)
            result = subprocess.run(cherry_pick_cmd)
            if result.returncode != 0:
                print ("...FAILED (cherry-pick --no-commit)")
                return
        
        commit_cmd = ["git", "commit", "-m", "PR {} - {}".format(number, title)]
        result = subprocess.run(commit_cmd)
        if result.returncode != 0:
            print ("...FAILED (commit)")
            return
            

def get_commits():
    commits = []

    # # PR 666 - Immediate Mode Integration - Take 2
    # commits.extend([
    #     "d2bbb435e160e447776e8b0c068bce0a00e8f78d",
    #     "58fdb8358dba361ef41510f09810f06691ff0ba3",
    #     "d0aa9618344cd9098adf7b667b82efd18af9ea56",
    #     "da6144279400d74b1e33b21dbac21c103dc6933f",
    #     "6db0a8a449d943f6a820e057f94487ff49b120ac",
    #     "62f1a5e5c060a6e2cf26ec8bc14f280ff12d3318",
    #     "124992d4244da538d6afe9bf9eb070d356848958",
    #     "e06fb71b21e10f0895ca87af9641e45b8002d20f"
    # ])

    # # PR 726 - cherry-picking an Immediate Mode optimization from the r1.15-rocm stream
    # commits.extend([
    #     "7ca59ba5bbd1f2179dccc1ec611c470c6dbc6086",
    #     "55959f061c467bb139f80d69e2c66456c748ff16",
    # ])
    
    return commits
    
        
def cherry_pick_commits():

    for commit in get_commits():
        cherry_pick_cmd = ["git", "cherry-pick", commit]
        # print (cherry_pick_cmd)
        result = subprocess.run(cherry_pick_cmd)
        if result.returncode != 0:
            print ("...FAILED (cherry-pick)")
            return

        
if __name__ == "__main__" :
    cherry_pick_PRs()
    # cherry_pick_commits()
