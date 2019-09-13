#!/usr/bin/env bash

VMVER=`vmware --version | awk '{print $3}'`
VER=15.1.0

cd ${HOME}/downloads
wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-${VER}.tar.gz
tar -xzf workstation-${VER}.tar.gz
cd vmware-host-modules-workstation-${VER}
make
sudo make install
