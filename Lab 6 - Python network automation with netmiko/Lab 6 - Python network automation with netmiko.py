#!/usr/bin/env python3

from netmiko import ConnectHandler, SSHDetect
from netmiko.exceptions import NetMikoTimeoutException
from netmiko.exceptions import AuthenticationException
from netmiko.exceptions import SSHException
from paramiko.ssh_exception import SSHException
from getpass import getpass
import datetime

#Define the device parameters
devices = [
{
    'device_type': 'cisco_ios',
    'host':   '172.16.4.49',
    'username': 'Michael',
    'password': 'pxl',
    'port' : 22,          
    'secret': 'pxl',
},
{
    'device_type': 'cisco_ios',
    'host':   '172.16.4.6',
    'username': 'Michael',
    'password': 'pxl',
    'port' : 22,          
    'secret': 'pxl',
}
]

# establish connection
for device in devices:
    # Establish an SSH connection to the device
    ssh = ConnectHandler(**device)
    ssh.enable()

# PART 1 #

# function to send a single show command and return the output
def send_show_command(command):
    output = ssh.send_command(command)
    return output

# Example
interface_status = send_show_command("show interfaces status")
print(interface_status)

# function to send multiple show commands and return the output
def send_multiple_show_commands(commands):
    output = ""
    for command in commands:
        output += ssh.send_command(command)
    return output

# Example
show_commands = ["show interfaces", "show version"]
show_output = send_multiple_show_commands(show_commands)
print(show_output)

# function to send multiple configuration commands and return the output
def send_multiple_config_commands(commands):
    output = ssh.send_config_set(commands)
    return output

# Example
config_commands = [
    "vlan 10",
    "name Management",
]
config_output = send_multiple_config_commands(config_commands)
print(config_output)

# PART 2 #

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
ip_addresses = ['172.16.4.49', '172.16.4.6']
commands = ['show interfaces', 'show ip route']

output = send_show_commands_to_multiple_devices(ip_addresses, commands)
print(output)

# function to send configuration commands to multiple devices
def send_config_commands_to_multiple_devices(ip_addresses, commands):
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
        output += ssh.send_config_set(commands)
        ssh.disconnect()

# Example
ip_addresses = ['172.16.4.49', '172.16.4.6']
commands = ['vlan 10', 'name Management']

send_config_commands_to_multiple_devices(ip_addresses, commands)

# Function to run show commands and save the output
def run_show_commands_and_save_output(ip_address, commands, filename):
    output = ""
    device = {
        'device_type': 'cisco_ios',
        'host': ip_address,
        'username': 'Michael',
        'password': 'pxl',
        'port': 22,
        'secret': 'pxl'
    }
    ssh = ConnectHandler(**device)
    ssh.enable()
    for command in commands:
        output += ssh.send_command(command)
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Output saved to {filename}")
    ssh.disconnect()
    return output

# Example
ip_address = '172.16.4.49'
commands = ['show interfaces', 'show ip route']
filename = 'output.txt'

run_show_commands_and_save_output(ip_address, commands, filename)

# Function to backup the device configurations
def backup_device_config(ip_address):
    output = ""
    device = {
        'device_type': 'cisco_ios',
        'host': ip_address,
        'username': 'Michael',
        'password': 'pxl',
        'port': 22,
        'secret': 'pxl'
    }
    ssh = ConnectHandler(**device)
    ssh.enable()
    output = ssh.send_command("show running-config")
    filename = f"{ip_address}_config_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, 'w') as f:
        f.write(output)
    print(f"Configuration saved to {filename}")
    ssh.disconnect()

# Example
ip_address = '172.16.4.49'

backup_device_config(ip_address)

# Function to configure a subset of Interfaces
def configure_interfaces(device_ip, interface_list):
    output = ""
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': 'Michael',
        'password': 'pxl',
        'port': 22,
        'secret': 'pxl'
    }
    with ConnectHandler(**device) as net_connect:
        for interface in interface_list:
            config_commands = [
                f"interface {interface}",
                "no shutdown",
            ]
            output = net_connect.send_config_set(config_commands)
            print(f"Configuration applied to {interface} on {device_ip}")
    net_connect.disconnect()

# Example
device_ip = '172.16.4.49'
interface_list = ['G0/1', 'G0/2']

configure_interfaces(device_ip, interface_list)

# Function to send configuration from a file
def send_config_file(device_ip, config_file):
    output = ""
    device = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': 'Michael',
        'password': 'pxl',
        'port': 22,
        'secret': 'pxl'
    }
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_from_file(config_file)
        print(f"Configuration applied to {device_ip}")
    net_connect.disconnect()

# Example
device_ip = '172.16.4.49'
config_file = 'config.txt'

send_config_file(device_ip, config_file)

# function to connect using a Python Dictionary
def connect_using_dict(device_dict):
    with ConnectHandler(**device_dict) as net_connect:
        output = net_connect.send_command('show version')
        print(output)
    net_connect.disconnect()

device_dict = {
        'device_type': 'cisco_ios',
        'host': '172.16.4.49',
        'username': 'Michael',
        'password': 'pxl',
        'port': 22,
        'secret': 'pxl'
}

# Example
connect_using_dict(device_dict)

# function to execute a script with a Function or classes
def execute_script(device_dict, script):
    with ConnectHandler(**device_dict) as net_connect:
        exec(script, {'net_connect': net_connect})

device_dict = {
    'device_type': 'cisco_ios',
    'host': '172.16.4.49',
    'username': 'Michael',
    'password': 'pxl',
    'port': 22,
    'secret': 'pxl'
}

script = '''
# Define your Cisco commands here
commands = [
    'show version',
    'show interfaces',
    'show ip route'
]

for command in commands:
    output = net_connect.send_command(command)
    print(output)
'''

execute_script(device_dict, script)

# function to execute a script with a statements (if, ifelse, else)
def execute_script_with_statements(device_dict, script):
    with ConnectHandler(**device_dict) as net_connect:
        exec(script)
    net_connect.disconnect()

device_dict = {
    'device_type': 'cisco_ios',
    'host': '172.16.4.49',
    'username': 'Michael',
    'password': 'pxl',
    'port': 22,
    'secret': 'pxl'
}

script = '''
x = 5
y = 10

if x > y:
    output = net_connect.send_command('show interfaces')
    print(output)
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")
'''

execute_script_with_statements(device_dict, script)