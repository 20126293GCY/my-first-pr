###################################################################################################
#
# Caesar Cipher program
#
# File:        caesar-cipher-week3.py
# Author:      20126293@tafe.wa.edu.au
# Copyright:   Copyright 2024
#
####################################################################################################

print("Welcome to Caesar cipher program")

name = input("What is your name?" )

print(name, "hope you enjoy encrypting and decrypting words.")

letter = input("Please give a letter to encrypt:  ")
shift = input("Shift by how many characters?: ")

try:
    shift = int(shift)
except:
    error = input("Shift should be a number, press ENTER to stop")
    quit()

if letter.isalpha():
    ascii_value = ord(letter)
    ascii_value = ascii_value + shift
    answer = chr(ascii_value)
    print("Caesar cipher letter is", answer)

else:
    print("You did not enter a letter to shift")


