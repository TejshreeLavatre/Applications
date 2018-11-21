# import the necessary modules
import random
import sys


def subnet_calc():
    while True:
        ip_address = input("Enter a valid IP address: ")

        a = ip_address.split(".")  # Splits the IP address into a list containing octets
        ''' IP address should have 4 octets. Addresses starting from 127 are reserved for 
        loop-back interfaces so we exclude them. Addresses starting from 169.254 are unable 
        to connect to the HTTP server so they are excluded as well.  
        '''

        if (len(a) == 4) \
                and (1 <= int(a[0]) <= 223) \
                and (int(a[0]) != 127) \
                and (int(a[0]) != 169 or int(a[1]) != 254) \
                and (0 <= int(a[1]) <= 255 and 0 <= int(a[2]) <= 255 and 0 <= int(a[3]) <= 255):
            break
            # or means multiplication. and means addition

        else:
            print("\nPlease enter a valid IP address.\n")
            continue

    masks = [255, 254, 252, 248, 240, 224, 192, 128, 0]

    # Is it a valid subnet mask?
    while True:
        subnet_mask = input("\nEnter a subnet mask:")

        # Check octets
        b = subnet_mask.split(".")

        if (len(b) == 4) \
                and (int(b[0]) == 255) \
                and (int(b[1]) in masks) \
                and (int(b[2]) in masks) \
                and (int(b[3]) in masks) \
                and (int(b[0]) >= int(b[1]) >= int(b[2]) >= int(b[3])):
            break

        else:
            print("\nPlease enter a valid subnet mask.\n")
            continue

    # Converting subnet mask into binary string format
    mask_octet_decimal = subnet_mask.split(".")
    mask_octet_padded = []
    for entry in range(0, len(mask_octet_decimal)):
        binary_octet = bin(int(mask_octet_decimal[entry])).split("b")[1]

        if len(binary_octet) == 8:
            mask_octet_padded.append(binary_octet)

        elif len(binary_octet) < 8:
            binary_octet_padded = binary_octet.zfill(8)
            mask_octet_padded.append(binary_octet_padded)

    decimal_mask = "".join(mask_octet_padded)
    # print("Decimal subnet mask is: ", decimal_mask)

    # Count host bits in subnet mask and calculate number of hosts per subnet
    no_of_zeroes = decimal_mask.count("0")
    no_of_ones = 32 - no_of_zeroes
    hosts_per_subnet = abs(2 ** no_of_zeroes) - 2  # To return positive value if mask is 32 bits
    # print("Number of zeroes: ", no_of_zeroes)
    # print("Number of ones: ", no_of_ones)
    # print("Number of hosts per subnet: ", hosts_per_subnet)

    # Wildcard mask
    """A wilcard mask is simply the inverse of the subnet mask"""
    wildcard_octet = []
    for entry in mask_octet_decimal:
        wildcard = 255 - int(entry)
        wildcard_octet.append(str(wildcard))

    wildcard_mask = ".".join(wildcard_octet)

    # Converting IP address to binary format
    padded_binary_IP = []
    for entry in a:
        binary_IP = bin(int(entry)).split("b")[1]

        if len(binary_IP) == 8:
            padded_binary_IP.append(binary_IP)

        elif len(binary_IP) < 8:
            binary_octets = binary_IP.zfill(8)
            padded_binary_IP.append(binary_octets)

    binary_IP_Address = "".join(padded_binary_IP)
    # print("Binary IP address: ", binary_IP_Address)

    # Finding Subnet ID and Broadcast Address
    binary_subnet_ID = binary_IP_Address[:no_of_ones] + "0" * no_of_zeroes
    binary_broadcast_address = binary_IP_Address[:no_of_ones] + "1" * no_of_zeroes
    # print(binary_subnet_ID)
    # print(binary_broadcast_address)
    subnet_ID_octet = []
    for entry in range(0, len(binary_subnet_ID), 8):
        subnet_octet = binary_subnet_ID[entry:entry + 8]
        subnet_ID_octet.append(subnet_octet)
    # print(subnet_ID_octet)

    string_subnet_ID = []
    for octet in subnet_ID_octet:
        string_subnet_ID.append(str(int(octet, 2)))

    final_subnet_ID = ".".join(string_subnet_ID)
    print("Subnet ID is: ", final_subnet_ID)


subnet_calc()
