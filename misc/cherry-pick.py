#! /usr/bin/python3

import subprocess

def get_PRs():
    PRs = []

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
    #         "f308b3206d8f9f2dd26168a1ebdb9fe738152891",
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
    #         "b84908da7797139892c68c7680375dd6389c71a0",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35519",
    #     "[ROCm] Unit-test updates for the ROCm platform.",
    #     [
    #         "195ccce69712e343eb7cd9466981ebdbf784cc3d",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35624",
    #     "[ROCm] Misc updates for the ROCm platform",
    #     [
    #         "09e2eaf34227ef922d8e85b0caef2c0eb5749df5",
    #         "d325b255ff7d0bf1ca04229880dffb0a37d52e2d",
    #         "17b87f0b51ad290269f983a85b887ae838c2ebe2",
    #         "04fb568df083a1903dd4f061539b29b4a849fd18",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35666",
    #     "[ROCm] Support for complex type BLAS operations",
    #     [
    #         "c329f1c5020c3df814be0a1e98cd740c5a4e4621",
    #         "543db6fc6713ed9ba19cf798a92f4bd2f4ad9ba2",
    #         "0f0aa375122dea501a237a5f8462bfde31d03a7d",
    #         "b64dde60e829387ce81bf88d0cb23402a9211245",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35752",
    #     "[ROCm] Fix the ROCm CSB breakage - 200110",
    #     [
    #         "f8ba03dfd976278a605e53ac741210fbab14c7ae",
    #     ]])

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
    #     "google_upstream",
    #     "35964",
    #     "[ROCm] Enabling //tensorflow/core/framework:variant_op_registry_test",
    #     [
    #         "c1b02f9a649cdd0793e667ccb7445d50e5095ceb",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35965",
    #     "[ROCm] Enabling the kernel Relu for float16",
    #     [
    #         "1087b24938690a5d747a6e51e6d00a10d039e898",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35966",
    #     "[ROCm] Complex sparse ops",
    #     [
    #         "815fa1866caa88727d2d5288c028f0e610c4bda3",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35971",
    #     "[ROCm] GpuManagedAllocator and common_runtime unit tests",
    #     [
    #         "af54994072bda083229fd11cb2b1d58e2cd38ab0",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35972",
    #     "Enabling several cwise op kernels for ROCm",
    #     [
    #         "d45988d245ada11dc2b1168e86f1d4441e0f844c",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "35991",
    #     "[ROCm][XLA] Updating amdgpu compiler and enabling llvm compiler test",
    #     [
    #         "7dd98d772edb141481775639fbcb9fbdd0a3d92a",
    #         "8a1f448f84b3e5a870b5fca34a91741e73acd928",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36017",
    #     "[ROCm] Fixing a bug in the previous commit to nccl_manager_test.cc file. ",
    #     [
    #         "cd1a77fd5e6438b825cc90bd34706a8edeea809a",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36018",
    #     "[ROCm] Changing cuda* names to gpu* names in a couple of tests",
    #     [
    #         "1a071541c184204fef1359e719586909de36f492",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36019",
    #     "[ROCm] Adding/Removing no_rocm tag to/from tests",
    #     [
    #         "1aa06e922f9a17e8fa333064da8846d860877894",
    #     ]])

    # # PRs.append([
    # #     "google_upstream",
    # #     "36031",
    # #     "[ROCm] Fix for compile error in //tensorflow/compiler/xla/service:dynamic_padder_test",
    # #     [
    # #         "3a5862c887f2df5030ef741c35c5600c90569771",
    # #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36032",
    #     "[ROCm] Fix for compile error in //tensorflow/compiler/xla:refcounting_hash_map_test",
    #     [
    #         "e6fa8e3e024d3c337124e977e64f1f63936ac5b7",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36106",
    #     "[ROCm] add ROCm support for XLA RCCL thunk",
    #     [
    #         "ab136158ca7b69f22f9225bae91887ed44d0e863",
    #     ]])

    # PRs.append([
    #     "google_upstream",
    #     "36110",
    #     "[ROCm][XLA] Adding address space cast in ir_emitter",
    #     [
    #         "d4c87aab1d61dd0ae53434ab03d4a887d868e023",
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
            

if __name__ == "__main__" :
    cherry_pick_PRs()
