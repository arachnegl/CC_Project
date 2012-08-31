"""
This is a script for Mac OSX to automate the installation of a Ubuntu virtual machine instance using the open source VirtualBox from Oracle.

It is the development environment that I use.

Tested on Mac OSX 10.6 "Snow Leopard" and 10.7 "Lion"

(it should work on a linux machine with minimal modifications)
"""

!/usr/bin/env python

import subprocess, os

print("#############################################")
print("This script creates a VBox Virtual Machine")
print("Please ensure that there is an iso copy in current dir (pwd)")
print("#############################################")

name = 'myVM'
userPath = yourhomepath                                  #  eg: "/Users/gregoryloyse/"

hd_name = name +'.vdi'                                   # name used for virtual hard drive

cwd = os.getcwd()
path_to_iso = cwd + "/ubuntu-12.04-server-amd64.iso"     #  eg: "/Users/gregoryloyse/ubuntu-12.04-server-amd64.iso"

# For network purposes:
adapter = subprocess.check_output("ifconfig | awk -F: '/^en/ { print $1 }'", shell=True).split()[0]

print("Will create VM called " + name + 
      " on harddrive " + hd_name + 
      " using iso image " + path_to_iso + 
      " and adapater " + adapter)

# Creating the instance:

subprocess.call([ "VBoxManage", "createvm", 
                  "--name", name, 
                  "-register", 
                  "--ostype", "Ubuntu_64"])
subprocess.call([ "VBoxManage", "createhd", 
                  "--filename", hd_name, 
                  "--size", "8000", 
                  "--variant", "Fixed"])
subprocess.call([ "VBoxManage", "storagectl", name, 
                  "--name", "IDE Controller", 
                  "--add", "ide", 
                  "--controller", "PIIX4"])
subprocess.call([ "VBoxManage", "storageattach", name, 
                  "--storagectl", "IDE Controller", 
                  "--port", "0", 
                  "--device", "0", 
                  "--type", "hdd", 
                  "--medium", hd_name])
subprocess.call([ "VBoxManage", "storageattach", name, 
                  "--storagectl", "IDE Controller", 
                  "--port", "0", 
                  "--device", "1", 
                  "--type", "dvddrive", 
                  "--medium", path_to_iso])

"""
subprocess.call([ "VBoxManage", "modifyvm", name, 
                  "--nic1", "bridged", 
                  "--cableconnected1", "on", 
                  "--bridgeadapter1", adapter]) # this breaks dhcp config and dflt network address translation seems sufficient for my purposes
"""


subprocess.call([ "VBoxManage", "modifyvm", name, 
                  "--memory", "512"])


"""
# Wanted to set up port forwarding but unnecessary at this stage of project:
# frwrd localhost to VM
subprocess.call([ "VBoxManage", "modifyvm", name, 
                  "--natpf1", "guest_HTML,tcp,127.0.0.1,80,,80"])
"""


# port forwarding to enable ssh log in:
subprocess.call([ "VBoxManage", "modifyvm", name, 
                  "--natpf1", "guest_ssh,tcp,127.0.0.1,2222,,22"])


print("#############################################")
print("All done, Good Bye")
print("#############################################")

# Start the new VM
subprocess.call([ "VBoxManage", "startvm", name])

"""
# A cmd for adding controller:
# Usefull for installing a new instance
subprocess.call(["VBoxManage", "storageattach", name,
                 "--storagectl" "IDE Controller",
                 "--port", "0",
                 "--device", "1",
                 "--type", "dvddrive",
                 "--medium",path_to_iso])    
"""
