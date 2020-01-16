#! /usr/bin/python3

import subprocess


def get_PRs():
    PRs = []

    # # PRs.append([
    # #     "google_upstream",
    # #     "34800",
    # #     "[ROCm] Add ROCm support for CSR Sparse Matrix Ops",
    # #     [
    # #         "9e7eae9f71855efe83287977e1844806675adaee",
    # #         "f725b464549eab744148ad940e04060cbaa7ae90",
    # #         "5ad7620d6f18f4a3c123fb7f365f0cb20dda2760",
    # #         "7e8ccbd22be53cade35de31631a8ada0bccfbac5",
    # #         "2e1cdaa4b62103d1d6f2e18845bbc2c69ffc117b",
    # #         "e762347e79f10f0ee3a730385f4959808ec2fb1e",
    # #         "5d1ccc1eeeebd527427ff02c24b7a967861e2868",
    # #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35394",
    #     "[ROCm] Support of GRU and LSTM",
    #     [
    #         "75a65d44e9fb7bc2ca94e1d17fa71e48aff739cb",
    #         "58f96c08e561c1ad1280c5264ff2c769cad8f7b3",
    #         "5afa56da8e0e2f64ec8df55d66eb8ce535f710c9",
    #         "d8e50e6613aa44803df63ff9f288abcf7580ccb1",
    #         "8a35d335bc917fd3452032e594c6dab7459a19f8",
    #         "ababeaabc08215b5d2809d49c8652e2ad6a01543",
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
    #     "google_upstream",
    #     "35519",
    #     "[ROCm] Unit-test updates for the ROCm platform",
    #     [
    #         "f580a3debd6902383e44daba50ee6aaf0d49a4eb",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35572",
    #     "[ROCm] XLA unit-test updates for the ROCm platform",
    #     [
    #         "c14b6951de82cd4c4957ccb181ef2946a8309ff1",
    #         "11b85f74734aa3cc2df422aec8a758d91d2ae1e0",
    #         "88a1e3b399d7f46cc33ed9a6d14f1873e292bf36",
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
    #     "35666",
    #     "[ROCm] Support for complex type BLAS operations #35666",
    #     [
    #         "c329f1c5020c3df814be0a1e98cd740c5a4e4621",
    #         "543db6fc6713ed9ba19cf798a92f4bd2f4ad9ba2",
    #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35751",
    # #     "[XLA] Update the path for the LLVM FileCheck executable",
    # #     [
    # #         "f99e0cb70658f93885ce07600918e386d6a10017",
    # #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35752",
    #     "[ROCm] Fix the ROCm CSB breakage - 200110",
    #     [
    #         "f8ba03dfd976278a605e53ac741210fbab14c7ae",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35764",
    #     "[ROCm] Minor updates to sync some of the ROCm fork contents ",
    #     [
    #         "bbe6c4b4ef839ce45362c4882eb335aa7577eefe",
    #         "a6c9e23a9ff887eb571b320e070a53bbd194c6d8",
    #         "6e7be1f6a55fe35f82b7c8c94014b31811cfad88",
    #         "8923d8d389e10ff2efd32f86e1e03c553a74757c",
    #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35779",
    # #     "[ROCm] Reenable the zero division test",
    # #     [
    # #         "38ecda3528b87630752d66a983b82656d31e9984",
    # #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35780",
    # #     "[ROCm] Add a GPU kernel for RELU int8x4",
    # #     [
    # #         "d1f1d78b86465a2c74a01464c96e36953be3ed79",
    # #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35832",
    # #     "[ROCm] Fix for the ROCm CSB breakage - 200113 - ",
    # #     [
    # #         "212eeb3732404cffc31504293019d18e79051218",
    # #         "473d15a87f28793d34d943ae104da696b9176554",
    # #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35834",
    # #     "[ROCm] Fix the ROCm CSB breakage - 200113 - 2",
    # #     [
    # #         "6e6791db417afd4266f051db533ce585db471f94",
    # #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "35881",
    # #     "[ROCm][XLA] Adding address space cast to generate correct llvm",
    # #     [
    # #         "9e657d7223869174ffe683de41b70b229db75ca5",
    # #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35890",
    #     "[ROCm] Fix for //tensorflow/python/kernel_tests/signal:mel_ops_test",
    #     [
    #         "3c7596fc76855b07125cbfa9eb2a7a093ee8719c",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35891",
    #     "[ROCm] Fix for //tensorflow/python/eager/benchmarks/resnet50:*",
    #     [
    #         "ee1c2f112dc666a19e0d9e4ad679c0e948ebde8a",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35924",
    #     "[ROCm] Optimized training apply ops",
    #     [
    #         "3693256ba03f67d38fe33daa495b296d45539076",
    #     ]])

    # PRs.append([
    #     "",
    #     "",
    #     "",
    #     [
    #     ]])

    #######################################################
    
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
    #         "418633269838d525b81f54d40c66a79ee544975c",  # need to rebase this commit
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
    #         "a9afccad8fce9a350168ecb1dc5591b64a982d41",  # need to rebase this commit
    #         "279bd153aa8301164d0b83efd54f0b13f8585368",
    #         "2680fa591e24e3e8ced3022ed72a1a396b018db9",
    #         "cbb9e56c07f9249603741950ceacd29914e94de0",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "791",
    #     "[DO NOT MERGE] Porting ROCm githooks to the master-rocm-enhanced branch",
    #     [
    #         "9c8604f7d367a0e7f21bcd3536b634f666dc88f5",
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
    #     "rocm_fork",
    #     "799",
    #     "[DO NOT MERGE] Porting ROCm batch_gemm support to master-rocm-enhanced",
    #     [
    #         "0e2126f1f74139c9c8e5c860e02cbbc4dae9fa3e"
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "803",
    #     "[DO NOT MERGE] Porting 3d pooling support to master-rocm-enhanced",
    #     [
    #         "64607bbd755ab61edcc55006ce15ceb8fdefffc2",
    #         "d210cfd869f620bea62d045c39a7ac0d235e628b",
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
