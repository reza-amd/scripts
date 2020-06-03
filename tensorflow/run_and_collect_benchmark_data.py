#!/usr/bin/env python3

import argparse
import json
import os
import re
import subprocess
import sys

from datetime import datetime

os.environ["HIP_VISIBLE_DEVICES"]="0";

def run_shell_command(cmd):
    print (" ".join(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # if result.returncode != 0:
    #     print("FAILED - {}".format(" ".join(cmd)))
    #     print("         {}".format(result.stdout.decode()))
    #     print("         {}".format(result.stderr.decode()))
    return result


def run_tf_cnn_benchmark(model, options):

    run_benchmark_cmd = [
        "python3",
        "scripts/tf_cnn_benchmarks/tf_cnn_benchmarks.py",
        "--model={}".format(model),
    ]
    for option in options:
        run_benchmark_cmd.append(option)

    result = run_shell_command(run_benchmark_cmd)
    return (result.returncode, result.stdout.decode(), result.stderr.decode())



def collect_tf_cnn_benchmark_perf_data():

    models = [
        "alexnet",
        "googlenet",
        "inception3",
        "inception4",
        "lenet",
        # "mobilenet",
        # "nasnet",
        # "nasnetlarge",
        # "ncf",
        # "overfeat",
        "resnet50",
        "resnet50_v1.5",
        "resnet101",
        "resnet152_v2",
        # "trivial",
        "vgg11",
        "vgg16",
        "vgg19",
    ]

    configs = [
        ("xla_OFF", []),
        ("xla_ON", ["--xla"]),
    ]
    
    N = 3
    
    data = {}
    data["models"] = models
    data["configs"] = configs
    data["N"] = N
    
    def run_N_times(N, model, options=[]):
        config_data = {}
        for i in range(N):
            run_data = run_tf_cnn_benchmark(model, options)
            config_data["run_{}".format(i)] = run_data
        return config_data

    for model in models:
        for name, options in configs:
            config_data = run_N_times(N, model, options)
            data["{}_{}".format(model, name)] = config_data

    return data


def gather_stats(data):

    models = data["models"]
    configs = data["configs"]
    N = data["N"]
    
    stats = {}

    def get_stats(N, config_data):
        run_stats = []
        for i in range(N):
            returncode, stdout, stderr = config_data["run_{}".format(i)]
            if returncode == 0:
                pattern = r'total images/sec: ([0-9\.]+)'
                match = re.search(pattern, stdout)
                assert(match is not None)
                run_stats.append(float(match.group(1)))
            else :
                run_stats.append("error")
        return run_stats
    
    for model in models:
        model_stats = {}
        for name, options in configs:
            config_data = data["{}_{}".format(model, name)]
            model_stats[name] = get_stats(N, config_data)
        stats[model] = model_stats

    return stats


def dump_stats(stats):
    print (stats)

if __name__ == '__main__':
           
    now = datetime.now()
    filename = "bm_data_{}.json".format(now.strftime("%y%m%d_%H%M"))
    print (filename)
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dump_stats_from", default=None)
    args = parser.parse_args()

    if (args.dump_stats_from):
        filename = args.dump_stats_from
        with open(filename) as f:
            data = json.loads(f.read())
            stats = gather_stats(data)
            dump_stats(stats)

    else :
        data = collect_tf_cnn_benchmark_perf_data()
        with open(filename, "w") as f:
            f.write(json.dumps(data))
