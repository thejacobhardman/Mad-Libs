# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 4/3/19
# Python Version 3.7.3

# Importing pkgs
import os
import sys

# Clears the screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

########################################################## GLOBAL VARIABLES ##############################################################

# Tracks if the program is still running
Is_Running = True

# Stores the User's input
User_Input = ""

# Tracks if the User has made a decision
User_Confirm = False

########################################################### PROGRAM LOGIC ################################################################

### Loads the Mad Libs file and prompts the User to enter the relevant information
def Load_File():

    # Importing global variables
    global User_Input
    global User_Confirm

    input("Press 'enter' to continue.")


########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:

    # Clearing the screen for readability
    cls()

    print("Welcome to Mad Libs!".center(80, " "))
    print("\nPlease enter the requested information to generate your custom Mad Lib.")

    Load_File()

    while User_Confirm == False:
        User_Input = input("\nWould you like to play again? (y/n): ")
        if User_Input.upper() == "Y":
            break
        elif User_Input.upper() == "N":
            Is_Running = False
            break
        else:
            print("Please enter a valid selection.")

    input("\nPress 'enter' to continue.")