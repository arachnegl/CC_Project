#!/usr/bin/zsh

# This is the environment setup script that I used to develop the project

# make this file excutable:
# chmod +x thisfile.sh

# matplotlib dependencies:
# sudo apt-get build-dep python-matplotlib   (450mb of deps!)
# I suspect you may only need the tk8 dep
# but there is a lot of tex stuff that may also be useful

PRJCT_NAME='py4maths'
WORK_DIR='maths'

echo ""
echo "*********************************************"
echo "                   WELCOME"
echo "*********************************************"
echo ""
echo "This script will set up a working environment for"
echo "scientific work 'a la python' "
echo "It includes git setup"
echo ""
echo ""
echo "*********************************************"
echo "INSTALLING AND ACTIVATING VIRTUAL ENVIRONMENT"
echo "*********************************************"
echo ""

virtualenv $PRJCT_NAME
cd $PRJCT_NAME
mkdir $WORK_DIR    # create future work dir
source bin/activate

echo ""
echo ""
echo "*********************************************"
echo "Installing packages"
echo "*********************************************"
echo ""
pip install yolk
# pip install readline   # unnecesary for Linux as support builtin
# pip install tornado    # dep for ipython notebook
# pip install pyzmq      # dep for ipy ntbk but need to install deps
pip install ipython
pip install numpy
pip install scipy
pip install matplotlib

clear
echo ""
echo ""
echo "*********************************************"
echo "INITIALISING GIT"
echo "*********************************************"
echo ""

cd $WORK_DIR
git init
cat <<EOF > README
This is a fresh install of python for maths in a virtual environment.
To start type: 'source bin/activate' in the current directory

Add documentation here.
EOF
cp ../../py4mathsVirtEnvSetup.sh .   # cpy this file & commit
git add README
git add py4mathsVirtEnvSetup.sh
git commit README py4mathsVirtEnvSetup.sh -m 'initial commit'
git log

# clear

echo ""
echo ""
echo "*******************************************"
echo "THESE PACKAGES ARE NOW INSTALLED IN VIRTENV"
echo "*******************************************"
echo ""

yolk -l

echo ""
echo ""
echo "*******************************************"
echo "These commands activate the environment:"
echo "*******************************************"
echo ""
echo "% source py4maths/bin/activate"
echo "% cd py4maths/maths"

echo ""
echo ""
echo "*******************************************"
echo "Lets draw a basic sin plot in matlab style:"
echo "*******************************************"
echo ""
# taken from matplotlib documentation
echo "% ipython --pylab"

echo "In [1] import numpy as np"
echo "In [2] import matplotlib.pyplot as plt"
echo "In [3] x = np.arrange(0,5,0.1)"
echo "In [4] y = np.sin(x)"
echo "In [5] plt.plot(x,y)"

echo ""
echo ""
echo "*******************************************"
echo "               GOOD BYE"
echo "*******************************************"
echo ""
