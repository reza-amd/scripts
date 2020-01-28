#! /usr/bin/python3

import subprocess

def get_PRs():
    PRs = []

    PRs.append([
        "google_upstream",
        "35394",
        "[ROCm] Support of GRU and LSTM",
        [
            "ae0e325a9fd53f2981bc569a2e3f8699c72a2ddc",
        ]])

    PRs.append([
        "google_upstream",
        "35395",
        "[ROCm] stateful random ops",
        [
            "968a674ecb6db34e5d2e09068a8d9ca5ca4e3e24",
            "f7b28191777b6ae86c0dbdab7a74b8370e53eaa8",
            "eee5851777b842945b12937600b005a58aae0f2c",
            "3122804c8537e920c4cfd2b92c141fd400fabe19",
            "b84908da7797139892c68c7680375dd6389c71a0",
        ]])

    PRs.append([
        "google_upstream",
        "35519",
        "[ROCm] Unit-test updates for the ROCm platform.",
        [
            "59b57bb4765d08d397d80e5aad17a7800a34c906",
        ]])

    PRs.append([
        "google_upstream",
        "35624",
        "[ROCm] Misc updates for the ROCm platform",
        [
            "09e2eaf34227ef922d8e85b0caef2c0eb5749df5",
            "d325b255ff7d0bf1ca04229880dffb0a37d52e2d",
            "17b87f0b51ad290269f983a85b887ae838c2ebe2",
            "04fb568df083a1903dd4f061539b29b4a849fd18",
        ]])

    PRs.append([
        "google_upstream",
        "35666",
        "[ROCm] Support for complex type BLAS operations",
        [
            "c329f1c5020c3df814be0a1e98cd740c5a4e4621",
            "543db6fc6713ed9ba19cf798a92f4bd2f4ad9ba2",
            "0f0aa375122dea501a237a5f8462bfde31d03a7d",
            # "b64dde60e829387ce81bf88d0cb23402a9211245",
        ]])

    PRs.append([
        "google_upstream",
        "35752",
        "[ROCm] Fix the ROCm CSB breakage - 200110",
        [
            "f8ba03dfd976278a605e53ac741210fbab14c7ae",
        ]])

    PRs.append([
        "google_upstream",
        "35890",
        "[ROCm] Fix for //tensorflow/python/kernel_tests/signal:mel_ops_test",
        [
            "3c7596fc76855b07125cbfa9eb2a7a093ee8719c",
        ]])

    PRs.append([
        "google_upstream",
        "35924",
        "[ROCm] Optimized training apply ops",
        [
            "3693256ba03f67d38fe33daa495b296d45539076",
        ]])

    PRs.append([
        "google_upstream",
        "35964",
        "[ROCm] Enabling //tensorflow/core/framework:variant_op_registry_test",
        [
            "c1b02f9a649cdd0793e667ccb7445d50e5095ceb",
        ]])

    PRs.append([
        "google_upstream",
        "35965",
        "[ROCm] Enabling the kernel Relu for float16",
        [
            "1087b24938690a5d747a6e51e6d00a10d039e898",
        ]])

    PRs.append([
        "google_upstream",
        "35966",
        "[ROCm] Complex sparse ops",
        [
            "815fa1866caa88727d2d5288c028f0e610c4bda3",
        ]])

    PRs.append([
        "google_upstream",
        "35971",
        "[ROCm] GpuManagedAllocator and common_runtime unit tests",
        [
            "af54994072bda083229fd11cb2b1d58e2cd38ab0",
        ]])

    PRs.append([
        "google_upstream",
        "35972",
        "[ROCm] Enabling several cwise op kernels",
        [
            "d45988d245ada11dc2b1168e86f1d4441e0f844c",
        ]])

    PRs.append([
        "google_upstream",
        "35991",
        "[ROCm][XLA] Enabling llvm compiler test",
        [
            "dfd7758505713de339367486741e7c24d0693490",
            "b27daf6d733ec695b64ad6a66508aeead918dbcc",
        ]])

    PRs.append([
        "google_upstream",
        "36017",
        "[ROCm] Fixing a bug in the previous commit to nccl_manager_test.cc file. ",
        [
            "cd1a77fd5e6438b825cc90bd34706a8edeea809a",
        ]])

    PRs.append([
        "google_upstream",
        "36106",
        "[ROCm] add ROCm support for XLA RCCL thunk",
        [
            "ab136158ca7b69f22f9225bae91887ed44d0e863",
        ]])

    PRs.append([
        "google_upstream",
        "36187",
        "[ROCm][XLA:GPU] Fixing Atomic CAS codegen in ir_emitter",
        [
            "c636d349510b6b1c480d2320bcbb21b51b4a005a",
        ]])

    PRs.append([
        "google_upstream",
        "36191",
        "[ROCm][XLA] Adding three passes to  amdgpu compiler",
        [
            "9d3d2d3b3e4d8ef139970460490e30c11a29540b",
        ]])

    PRs.append([
        "google_upstream",
        "36263",
        "[ROCm] Adding ROCm support for CTC Loss",
        [
            "d7dbb77bd663aaa016efc9cf350169f418b0905d",
        ]])

    PRs.append([
        "google_upstream",
        "36267",
        "[ROCm] Reverting ROCm to use MIOpen Find Mode APIs (be default) for convolution",
        [
            "d5eb53b58e1cbecb4ef233ae68dbdd82256d28db",
            "bdeac49239452228a3a0b58d33068b48f01a1756",
            "dd74624b082b002cbe90eca367518e6bdf673228",
            "8a44cb798fd10e619b84e78f9e6f6a273bc24c0a",
            "3cb4a728f876895c91204bf7ad626a583e38e726",
            "1d6a1be33fd3050d419b88a783828e969af8720e",
            "f3714797020720650ede00a1defbc75fca845986",
            "1dde494b6399cf0fde6a426ca64dcddb97ad17a0",
            "f7befd30d1e0f685ee1f8adbf2282e84b517025d",
            "5e8c52d82a1db999e487afedf401609be0b5f565",
        ]])

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
    #         "418633269838d525b81f54d40c66a79ee544975c",
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
    #         "0e2126f1f74139c9c8e5c860e02cbbc4dae9fa3e",
    #     ]])

    # PRs.append([
    #     "rocm_fork",
    #     "803",
    #     "[DO NOT MERGE] Porting 3d pooling support to master-rocm-enhanced",
    #     [
    #         "64607bbd755ab61edcc55006ce15ceb8fdefffc2",
    #         "d210cfd869f620bea62d045c39a7ac0d235e628b",
    #     ]])

    return PRs




def get_commit_specific_options(commit):
    commit_specific_options = {}
    commit_specific_options["c329f1c5020c3df814be0a1e98cd740c5a4e4621"] = ["-Xtheirs"]
    return commit_specific_options.get(commit, [])


def cherry_pick_PRs():

    for repo, number, title, commits in get_PRs():
        
        print ("Cherry-picking PR {} - {}".format(number, title))
        
        for commit in commits:
            cherry_pick_cmd = ["git", "cherry-pick", "--no-commit", commit]
            cherry_pick_cmd.extend(get_commit_specific_options(commit))
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


if __name__ == "__main__" :
    # cherry_pick_PRs()
    cherry_pick_commits()
