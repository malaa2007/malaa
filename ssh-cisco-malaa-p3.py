#########################################################################################################
##      Author = Mohamed Alaa                                                                          ##
##      Purpose = Simple SSH session to a Cisco router that executes the 'show ip int brief' command.  ##
##      Uses = netmiko, ConnectHandler                                                                 ##
##      Created on 2-10-2017                                                                           ##
##      Version 1.0                                                                                    ##
#########################################################################################################
#######################################################################################
##       __  __       _                              _      _    _                   ##
##      |  \/  | ___ | |__   __ _ _ __ ___   ___  __| |    / \  | | __ _  __ _       ##
##      | |\/| |/ _ \| '_ \ / _` | '_ ` _ \ / _ \/ _` |   / _ \ | |/ _` |/ _` |      ##
##      | |  | | (_) | | | | (_| | | | | | |  __/ (_| |  / ___ \| | (_| | (_| |      ##
##      |_|  |_|\___/|_| |_|\__,_|_| |_| |_|\___|\__,_| /_/   \_\_|\__,_|\__,_|      ##
##                                                                                   ##
#######################################################################################

## First, I must import the ConnectHandler factory function from Netmiko. 
## This factory function selects the correct Netmiko class based upon the device_type
 
from netmiko import ConnectHandler

## Request your inputs

IP = input("Enter Device IP Add: ")
USERNAME = input("Enter your Username: ")
PASSWORD = input("Enter your Password: ")
ENABLEPASS = input("Enter your enable password: ")

## Now in order to connect, all I need to do is call the "ConnectHandler" netmiko factory function directly
## The supported device_type's are cisco_ios, cisco_xe, cisco_asa, cisco_nxos, cisco_xr, cisco_wlc_ssh, arista_eos, 
## hp_procurve, hp_comware, huawei, f5_ltm, juniper, and brocade_vdx.

net_connect = ConnectHandler(device_type='cisco_ios', ip=IP, username=USERNAME, password=PASSWORD) 

## Now at this point we have an SSH connection. I can verify this by executing the .find_prompt() method

net_connect.find_prompt()

## I can also send commands down the SSH channel and receive the output back. 
## Here, I use the .send_command() method to send the 'show ip int brief' command:

output = net_connect.send_command("show ip int brief")

## Print the output of the command

print (output)