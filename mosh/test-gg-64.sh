#!/bin/bash -ex

${TIMECOMMAND_PREP} gg-run make -j64

export GG_MAXJOBS=64
${TIMECOMMAND} gg-reduce src/frontend/mosh-server src/frontend/mosh-client
