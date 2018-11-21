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


    # Converting mask into binary format
    


subnet_calc()
