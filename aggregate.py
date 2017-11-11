#!/usr/bin/env python3

import os
import sys
import numpy
import pprint

def usage():
    print("aggregate <results-dir> <expr-count>")

def main(results_dir, expr_count):
    points = []
    exec_points = []

    for i in range(expr_count):
        file_path = os.path.join(results_dir, '{}.timelog'.format(i))

        with open(file_path) as fin:
            for line in fin:
                line = line.strip()
                if len(line) == 0:
                    return

                points += [int(line.split(",")[1])]
                exec_points += [int(line.split(",")[2])]


    pprint.pprint({
        'avg': numpy.mean(points),
        'std': numpy.std(points),
        'min': min(points),
        'max': max(points),
        'median': numpy.median(points)
    })

    points = exec_points

    pprint.pprint({
        'avg': numpy.mean(points),
        'std': numpy.std(points),
        'min': min(points),
        'max': max(points),
        'median': numpy.median(points)
    })


if __name__ == "__main__":
    if len(sys.argv) < 3:
        usage()
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
