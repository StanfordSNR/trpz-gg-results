#!/bin/bash -ex

source ${BASH_SOURCE%/*}/define.sh

gg-init
${TIMECOMMAND_PREP0} gg-infer make -j${SMALL_CORES}

export GG_WHISK=1
export GG_MAXJOBS=${WSK_CORES}
export WSK_TIMELOG="${WSK_TIMELOG}"

${TIMECOMMAND} gg-force ${__GG_TARGETS?"not set"}
