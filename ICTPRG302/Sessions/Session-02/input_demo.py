#############################################################################
#
# Input Demo
#
# YOU CAN ADD DESCRIPTION LATER
#
# File:      Source/Repos/ICTPRG302/Sessions/Sessions-02/input_demo.py
# Author:    Gian Carlo Yu <20126293@tafe.wa.edu.au>
# Version:   1.0
#
# Copyright: © Copyright 2024, Gian Carlo Yu
#
#############################################################################

# Define Constants (ALL CAPS!)
WELCOME= "HELLO! "

# Define Variables
name = ""
second_name = ""
# Ask the user for their name
# then display a welcome message
name = input("What is your name? ")
second_name = input("What is the other person's name? ")
print(WELCOME + name + " and " + second_name)
