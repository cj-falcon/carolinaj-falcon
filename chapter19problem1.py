#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cjfalcon-argot
#
# Created:     09/09/2025
# Copyright:   (c) cjfalcon-argot 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def readposint():
    try:
        n = int(input("Enter a positive number: "))
        if n >=0:
            print("Your number is:", n)
        elif n<0:
            raise ValueError("Your number is negative number!")
    except:
        print("Your input is illegal!")

readposint()
