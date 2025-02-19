'''
Program Name: get_machine.py
Contact(s): Mallory Row
Abstract: This script is run by set_up_verif_global.sh.
          It gets the name of the name of the machine being
          run on by checking environment variables "machine"
          or "MACHINE". If not does matching based on environment
          variable "HOSTNAME" or output from hostname executable.
'''

import sys
import os
import re
import subprocess

print("BEGIN: "+os.path.basename(__file__))

EMC_verif_global_machine_list = [
    'HERA', 'ORION', 'S4', 'JET', 'WCOSS2', 'HERCULES', 'GAEAC5', 'GAEAC6'
]

# Read in environment variables
if not 'HOSTNAME' in list(os.environ.keys()):
    hostname = subprocess.check_output(
        'hostname', shell=True, encoding='UTF-8'
    ).replace('\n', '')
else:
    hostname = os.environ['HOSTNAME']

# Get machine name
for env_var in ['machine', 'MACHINE']:
    if env_var in os.environ:
        if os.environ[env_var] in EMC_verif_global_machine_list:
            print("Found environment variable "
                  +env_var+"="+os.environ[env_var])
            machine = os.environ[env_var]
            break
if 'machine' not in vars():
    hera_match = re.match(re.compile(r"^hfe[0-9]{2}$"), hostname)
    orion_match = re.match(
        re.compile(r"^orion-login-[0-9]{1}.hpc.msstate.edu$"), hostname
    )
    hercules_match = re.match(
        re.compile(r"^hercules-login-[0-9]{1}.hpc.msstate.edu$"), hostname
    )
    cactus_match = re.match(
        re.compile(r"^clogin[0-9]{2}$"), hostname
    )
    cactus_match2 = re.match(
        re.compile(r"^cdecflow[0-9]{2}$"), hostname
    )
    dogwood_match = re.match(
        re.compile(r"^dlogin[0-9]{2}$"), hostname
    )
    dogwood_match2 = re.match(
        re.compile(r"^ddecflow[0-9]{2}$"), hostname
    )
    s4_match = re.match(re.compile(r"s4-submit.ssec.wisc.edu"), hostname)
    jet_match = re.match(re.compile(r"^fe[0-9]{1}"), hostname)
    gaeac5_match = re.match(re.compile(r"^gaea5[0-9]{1}"), hostname)
    gaeac6_match = re.match(re.compile(r"^gaea6[0-9]{1}"), hostname)
    if cactus_match or dogwood_match or cactus_match2 or dogwood_match2:
        machine = 'WCOSS2'
    elif hera_match:
        machine = 'HERA'
    elif orion_match:
        machine = 'ORION'
    elif hercules_match:
        machine = 'HERCULES'
    elif s4_match:
        machine = 'S4'
    elif jet_match:
        machine = 'JET'
    elif gaeac5_match:
        machine = 'GAEAC5'
    elif gaeac6_match:
        machine = 'GAEAC6'
    else:
        print("Cannot find match for "+hostname)
        sys.exit(1)

# Write to machine config file
if not os.path.exists('config.machine'):
    with open('config.machine', 'a') as file:
        file.write('#!/bin/sh\n')
        file.write('echo "BEGIN: config.machine"\n')
        file.write('echo "Setting machine='+'"'+machine+'""\n')
        file.write('export machine='+'"'+machine+'"\n')
        file.write('echo "END: config.machine"')

print("Working "+hostname+" on "+machine)

print("END: "+os.path.basename(__file__))
