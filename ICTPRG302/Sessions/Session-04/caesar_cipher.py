###################################################################################################
#
# Caesar Cipher program
#
# File:        caesar-cipher-week3.py
# Author:      20126293@tafe.wa.edu.au
# Copyright:   Copyright 2024
#
####################################################################################################
def welcome():

    print("Welcome to Caesar cipher program")
    name = input("What is your name?" )
    print(name, "hope you enjoy encrypting and decrypting words.")
    return name

def encrypt(word, shift):
    message = ""
    for letter in word:
        ascii_value = ord(letter)+shift
        message = message + chr(ascii_value)
    return message

def get_shift():
    while True:
        number_to_shift = input("Shift by how many characters? ")
        try:
            number_to_shift = int(number_to_shift)
        except:
            print("Invalid shift")
            continue
        break
    return number_to_shift

def main():
    user = welcome()
    word = input("Word to encrypt: ")
    shift = get_shift()
    encrypt_message = encrypt(word, shift)
    print()
    print(user, "it is:")
    print("Word: ", word)
    print("Encrypted:", encrypt_message)

main()





