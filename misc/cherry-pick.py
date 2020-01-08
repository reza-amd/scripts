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
    #     # title before rebase: "[ROCm] Fix for the broken ROCm CSB - 200103",
    #     "[ROCm] XLA unit-test updates for the ROCm platform",
    #     [
    #         # commit before rebase: "ab527339f66193b4c22b10f95165c204ce459f11",
    #         # commit before rebase: "614babf5f56029ba8b173939ced0447b5f34b9fa",
    #         "7cc4b739812e2495e991d5925d758d3726f0ebaa",
    #         "1197d2c4ffff53a8cbc0b96138b37e76dd29a8b9",
    #         "3d78c04a46af6bcbc3a5dca6b49a5daa721457dd",
    #         "ed7df9cb4c9c5f3c6f5572b0b6eb3facefee55a3"
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "782",
    #     "[DO NOT MERGE] Porting ROCm Fusion support to master-rocm-enhanced",
    #     [
    #         "dff79b7d699dde6271ad8188c1c16e8dfdb43f3d",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "783",
    #     "[DO NOT MERGE] Porting ROCm blfoat16 support to master-rocm-enhanced",
    #     [
    #         # commit before rebase: "f5d29c6150117c27f7785bf8f7da63717f2c36ae",
    #         "418633269838d525b81f54d40c66a79ee544975c",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35624",
    #     "[ROCm] Misc updates for the ROCm platform",
    #     [
    #         "09e2eaf34227ef922d8e85b0caef2c0eb5749df5",
    #         "d325b255ff7d0bf1ca04229880dffb0a37d52e2d",
    #         "17b87f0b51ad290269f983a85b887ae838c2ebe2",
    #         "04fb568df083a1903dd4f061539b29b4a849fd18"
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35395",
    #     "[ROCm] stateful random ops",
    #     [
    #         "968a674ecb6db34e5d2e09068a8d9ca5ca4e3e24",
    #         "f7b28191777b6ae86c0dbdab7a74b8370e53eaa8",
    #         "eee5851777b842945b12937600b005a58aae0f2c",
    #         "3122804c8537e920c4cfd2b92c141fd400fabe19",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "789",
    #     "[DO NOT MERGE] Porting ROCm hipclang support to mater-rocm-enhanced",
    #     [
    #         "afe52fc3212b97d811d143b173ba68d494e26592",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "790",
    #     "[DO NOT MERGE] Porting ROCm Dropout support to master-rocm-enhanced",
    #     [
    #         "a9afccad8fce9a350168ecb1dc5591b64a982d41",
    #         "279bd153aa8301164d0b83efd54f0b13f8585368",
    #         "2680fa591e24e3e8ced3022ed72a1a396b018db9",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "791",
    #     "[DO NOT MERGE] Porting ROCm githooks to the master-rocm-enhanced branch",
    #     [
    #         "9c8604f7d367a0e7f21bcd3536b634f666dc88f5",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35394",
    #     "[ROCm] Support of GRU and LSTM",
    #     [
    #         "75a65d44e9fb7bc2ca94e1d17fa71e48aff739cb",
    #         "58f96c08e561c1ad1280c5264ff2c769cad8f7b3",
    #         "5afa56da8e0e2f64ec8df55d66eb8ce535f710c9",
    #         "d8e50e6613aa44803df63ff9f288abcf7580ccb1",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "794",
    #     "[DO NOT MERGE] Porting ROCm docs to master-rocm-enhanced",
    #     [
    #         "41b45a4405e47f785870c2da2733580e11e4b20c",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "795",
    #     "[DO NOT MERGE] Porting ROCm scripts to master-rocm-enhanced branch",
    #     [
    #         "7f5e9c8d5118eb72e473fa60ceb71ed6efffed30",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35666",
    #     "[ROCm] Support for complex type BLAS operations #35666",
    #     [
    #         "c329f1c5020c3df814be0a1e98cd740c5a4e4621",
    #         "543db6fc6713ed9ba19cf798a92f4bd2f4ad9ba2",
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
