#!/usr/bin/env python3

import os
import sys
import numpy
import pprint

from datetime import timedelta

PROGRAMS = ['mosh', 'git', 'vim', 'openssh']
EXPERIMENTS = ['gg-wsk-unsecure', 'gg-wsk-secure']

TIME_LINE = 'Elapsed (wall clock) time (h:mm:ss or m:ss): '

def parse_time(time_str):
    seconds = 0
    minutes = 0
    hours = 0

    d = time_str.split(':')

    seconds = float(d[-1])

    if len(d) > 1:
        minutes = int(d[-2])
    if len(d) > 2:
        hours = int(d[-3])
    if len(d) > 3:
        raise Exception("wrong time string: %s" % time_str)

    return timedelta(hours=hours, minutes=minutes, seconds=seconds)

def stats(numbers):
    return {
        'mean': numpy.mean(numbers),
        'median': numpy.median(numbers),
        'std': numpy.std(numbers)
    }

def aggregate(program, experiment, count=10):
    end_to_end = []
    all_lambdas = []
    total_lambdas = []
    exec_lambdas = []
    child_proc = []

    lambda_count = None

    root = os.path.join(program, experiment)

    for i in range(count):
        # read the end to end time
        this_lambdas = []

        with open(os.path.join(root, '%d.log' % i)) as fin:
            for line in fin:
                line = line.strip()
                if line.startswith(TIME_LINE):
                    end_to_end += [parse_time(line[len(TIME_LINE):]).total_seconds()]
                    break

        with open(os.path.join(root, '%d.timelog' % i)) as fin:
            for line in fin:
                line = line.strip()
                this_lambdas += [int(line.split(",")[1])]
                exec_lambdas += [int(line.split(",")[1])]
                child_proc += [int(line.split(",")[2])]

        with open(os.path.join(root, '%d.timelog.upload' % i)) as fin:
            for line in fin:
                line = line.strip()
                this_lambdas += [int(line.split(",")[1])]
                all_lambdas += [int(line.split(",")[1])]

        with open(os.path.join(root, '%d.timelog.download' % i)) as fin:
            for line in fin:
                line = line.strip()
                this_lambdas += [int(line.split(",")[1])]
                all_lambdas += [int(line.split(",")[1])]

        all_lambdas += exec_lambdas
        total_lambdas += [sum(this_lambdas)]

        if lambda_count == None:
            lambda_count = len(this_lambdas)
        else:
            assert lambda_count == len(this_lambdas)

    return {
        '1. end-to-end (s)': stats(end_to_end),
        '2. single lambda (ms)': stats(all_lambdas),
        '3. total lambda runtime (ms)': stats(total_lambdas),
        '4. lambda count': lambda_count
    }

for p in PROGRAMS:
    for e in EXPERIMENTS:
        print("// {} / {}\n".format(p, e))
        pprint.pprint(aggregate(p, e))
        print()
    print('/*' + ( '*' * 50 ) + '*/\n')
