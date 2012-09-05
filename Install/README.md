Installation Advice
===================

The software was developped on Ubuntu 12.04 using the python (v2.7) and prolog (Yap v7) programming languages.

Disaggregation requires python scientific libraries: ipython matplotlib and numpy.

For the abduction system you need an up to date version of the Yap for prolog (at least version 6) and [Jeifei's implementation of the ASystem](http://www-dse.doc.ic.ac.uk/cgi-bin/moin.cgi/abduction).



I have included various scripts here that I have used that may be of use to you.

If you have root access then these are available in Ubuntu's repositories. Simply issue:

    % sudo apt-get install python-matplotlib python-numpy ipython

and you should have everything you need


ipython console and the matplotlib and numpy libraries. (python scientific libraries which are lauded as equivalents for matlab-style work)



If you have root access to your repositories:

apt-get install...


Otherwise run the py4maths script

This will set up a virtual environment in a custom folder in your user space.

Finally you can also use the virtualbox environment that I have been using

Furthermore Ubuntu doesn't provide nice packages for an uptodate yap prolog. 
The script provided should ease that installation for you.