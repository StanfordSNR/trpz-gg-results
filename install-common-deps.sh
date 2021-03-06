#!/bin/bash -ex

sudo add-apt-repository -y ppa:keithw/gcc-backport
sudo apt-get update -qq

sudo apt-get install -y gcc-7 g++-7 automake autoconf libtool make curl \
                        unzip wget git pkg-config

sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 99
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 99
