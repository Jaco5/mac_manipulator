#!/usr/bin/env python

# Media Access Control (MAC) address changer.
# This program prompts the user for a new MAC address and what interface to assign it to.
# This helps maintain anonymity and allows impersonation.

# subprocess is a module that allows CLI interaction from the script.

import subprocess
import optparse
from random import seed
# from random import randint

seed

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Choose an interface, view options with ifconfig.")
parser.add_option("-m", "--mac", dest="new_MAC_address",
                  help="Choose an address 'aa:bb:cc:dd:ee:ff'.")

(options, arguments) = parser.parse_args()

# mac_array = ["10"]  # MAC addresses must start with an even number.
#
# for _ in range(5):
#     mac_element = str(randint(10, 99))
#     mac_array.append(mac_element)


interface = options.interface
new_MAC_address = options.new_MAC_address
# new_MAC_address = ":".join(mac_array)

print("[+] Changing MAC address for " + interface + " to " + new_MAC_address)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC_address])
subprocess.call(["ifconfig", interface, "up"])
