#!/bin/sh

clear
echo "INSTALLING DEPENDENCIES"

sudo apt-get install zsh emacs build-essential libreadline-dev \
    autoconf curl chrpath \
    ncurses-dev libreadline-dev libunwind7-dev \
    libgmp-dev \
    libxext-dev libice-dev libjpeg-dev libxinerama-dev libxft-dev \
    libxpm-dev libxt-dev pkg-config \
    libssl-dev \
    unixodbc-dev \
    zlib1g-dev libarchive-dev

clear
echo "MAKING THE TEMP FOLDER"
mkdir temp
cd temp

echo "NOW IN:"
pwd

clear
echo "NOW DOWNLOADING THE PROGRAM"
wget http://www.dcc.fc.up.pt/~vsc/Yap/yap-6.2.2.tar.gz 
tar -zxvf yap-6.2.2.tar.gz 
cd yap-6.2.2 
./configure 
make 
sudo make install 
cd .. 
rm -rf temp

echo "ALL DONE, BYE FOR NOW"