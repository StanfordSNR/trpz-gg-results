#!/bin/bash -x

export GG_S3_BUCKET=gg-ec2-us-west-2

./run-test llvm-minrel gg-ec2-64 5
./run-test llvm-minrel icecc-make-64 5

sleep 300

mv results/ results.0/
./run-test llvm-minrel gg-ec2-64 5