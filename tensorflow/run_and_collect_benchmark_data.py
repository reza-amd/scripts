#!/usr/bin/env python3

import argparse
import json
import os
import re
import subprocess
import sys

from datetime import datetime

from openpyxl import Workbook
from openpyxl.styles import Font

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
    stats["models"] = models
    stats["configs"] = configs
    stats["N"] = N

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


def dump_stats(excel_file, stats):

    workbook = Workbook()
    sheet = workbook.active

    workbook = Workbook()
    sheet = workbook.active

    models = stats["models"]
    configs = stats["configs"]
    N = stats["N"]
    
    header_1 = ["", ""]
    for name, options in configs:
        header_1.append(name)
        for i in range(N):
            header_1.append("")
        header_1.append("")
    # print (header_1)
    sheet.append(header_1)
    
    header_2 = ["benchmark", ""]
    for name, options in configs:
        for i in range(N):
            header_2.append("run_{}".format(i))
        header_2.append("AVERAGE") 
        header_2.append("") 
    # print (header_2)
    sheet.append(header_2)

    for model in models:
        row = [model, ""]
        model_stats = stats[model]
        for name, options in configs:
            config_stats = model_stats[name]
            for i in range(N):
                row.append(config_stats[i])
            row.append("")
            row.append("")
        # print(row)
        sheet.append(row)
            
    workbook.save(filename=excel_file)


if __name__ == '__main__':
           
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dump_stats_from", default=None)
    args = parser.parse_args()

    if (args.dump_stats_from):
        filename = args.dump_stats_from
        with open(filename) as f:
            data = json.loads(f.read())
            stats = gather_stats(data)
            dump_stats(filename.replace("json", "xlsx"), stats)

    else :
        data = collect_tf_cnn_benchmark_perf_data()
        now = datetime.now()
        filename = "bm_data_{}.json".format(now.strftime("%y%m%d_%H%M"))
        with open(filename, "w") as f:
            f.write(json.dumps(data))
