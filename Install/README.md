Installation Advice
===================

As a convenience I have included various scripts here that I have used and that may be of use to you.

The software was developped on Ubuntu 12.04 using the python (v2.7) and prolog (Yap v7) programming languages.

The disaggregation part of this project requires python scientific libraries: ipython matplotlib and numpy. These can be described as 'matlab equivalents' for python.

The abduction part of this project requires an up to date version of the Yap prolog compiler (at least version 6) and [Jeifei's implementation of the ASystem](http://www-dse.doc.ic.ac.uk/cgi-bin/moin.cgi/abduction). Caution: the version of Yap in Ubuntu's 12.04 repository is not sufficiently up to date. You need to install it by compiling it. An option is to use the script provided.



*   If you have root access then these are available in Ubuntu's repositories. Simply issue:

            % sudo apt-get install python-matplotlib python-numpy ipython

*   If you can't or don't want to do a system wide installation using official repositories then virtualenv provides a suitable up to date environment in your user directory. See the python4maths.sh script provided. 
*   Virtualbox can be used in addition or in combination with the above options., you can also use virtualbox to fully isolate your development environment. This is what I have used.