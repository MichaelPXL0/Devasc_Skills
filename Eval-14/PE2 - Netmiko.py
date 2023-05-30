#!/usr/bin/env python3

from netmiko import ConnectHandler, SSHDetect
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from paramiko.ssh_exception import SSHException
from getpass import getpass
import datetime

# establish connection
for device in devices:
    # Establish an SSH connection to the device
    ssh = ConnectHandler(**device)
    ssh.enable()

# function to send show commands to multiple devices
def send_show_commands_to_multiple_devices(ip_addresses, commands):
    output = ""
    for ip_address in ip_addresses:
        device = {
            'device_type': 'cisco_ios',
            'host': ip_address,
            'username': 'Michael',
            'password': 'pxl',
            'port' : 22,
            'secret': 'pxl'
        }
        ssh = ConnectHandler(**device)
        ssh.enable()
        for command in commands:
            output += ssh.send_command(command)
        ssh.disconnect()
    return output

# Example
ip_addresses = ['172.16.4.2', '172.16.4.6']
commands = ['show ip interfaces']

output = send_show_commands_to_multiple_devices(ip_addresses, commands)
print(output)