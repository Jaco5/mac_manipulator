#!/usr/bin/env python

# Media Access Control (MAC) address changer.
# This program prompts the user for a new MAC address and what interface to assign it to.
# This helps maintain anonymity and allows impersonation.
# Input interface type using -i or --interface.
# Input a mac address or leave input blank to generate random.

# subprocess is a module that allows CLI interaction from the script.

import subprocess
import optparse
from random import seed
from random import randint

seed

parser = optparse.OptionParser()

parser.add_option("-i", "--interface",
                  dest="interface",
                  help="Choose an interface, view options with ifconfig.")
parser.add_option("-m", "--mac",
                  dest="new_MAC_address",
                  help="Choose an address 'aa:bb:cc:dd:ee:ff', or leave argument out to generate random.")

(options, arguments) = parser.parse_args()


def generate_mac_address():
    for _ in range(5):
        mac_element = str(randint(10, 99))
        mac_array.append(mac_element)


if options.interface:
    interface = options.interface
else:
    print("[readme] You may supply arguments when calling the script, see help. ")
    interface = input("[i] choose an interface >")


if options.new_MAC_address:
    new_MAC_address = options.new_MAC_address
    print("[!] input address used")
else:
    evenNum = input("[i] choose an even number 'xx' ")
    mac_array = [evenNum]  # MAC addresses must start with an even number.
    generate_mac_address()
    new_MAC_address = ":".join(mac_array)
    print("[!] random MAC address generated")


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC_address])
subprocess.call(["ifconfig", interface, "up"])

print("[+] changing MAC address for " + interface + " to " + new_MAC_address)