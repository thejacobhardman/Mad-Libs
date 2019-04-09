# Jacob Hardman
# Intro To Programming
# Professor Marcus Longwell
# 4/3/19
# Python Version 3.7.3

# Importing pkgs
import os

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

# String that holds the complete User Story
User_Story = ""

########################################################### PROGRAM LOGIC ################################################################

### Loads the 'Outline.txt' file into the program
def Load_File():

    # Importing global variables
    global Is_Running
    global Outline

    # Loads the 'Outline.txt' file and closes the program if the file cannot be found by the program.
    try:
        Outline = open("Outline.txt","r")
    except:
        print("*ERROR* 'Outline.txt' file not found. *ERROR*")
        print("Please ensure that 'Outline.txt' is in the same folder as the 'MadLibs.py' file.")
        input("Press 'enter' to close the program.")
        Is_Running = False

### Prompts the User to enter information to customize the MadLibs
def Prompt_User():

    # Importing global variables
    global User_Input
    global User_Confirm
    global User_Story
    global Outline

    Line_Content = Outline.readline() # Reads what is in each line of the 'Outline.txt' file

    while Line_Content: # While there are still lines left to be read
        while "[" in Line_Content: # Parses through each line of 'Outline.txt' and finds every instance of '['
            Start = Line_Content.find("[") # Defining the borders of the text to be replaced
            End = Line_Content.find("]")
            Prompt = Line_Content[Start + 1:End] # Assinging the text to be replaced to a variable
            User_Input = input(Prompt + ": ") # Getting the text that the User wants to use to replace the placeholder text
            Line_Content = Line_Content.replace("[" + Prompt + "]", User_Input) # Replacing the placeholder with the User's text
        else: # Executes if there are no more instances of '[' on the current line
            User_Story = User_Story + Line_Content # Builds the completed story
            Line_Content = Outline.readline() # Moves on to the next line of 'Outline.txt'


### Displays the User their customized MadLibs
def Display_Story():

    # Importing global variables
    global User_Story

    # Clearing the screen for readability
    cls()

    print(User_Story)

### Exports the User's customized MadLibs into a new .txt file
def Export_Story():

    # Importing global variables
    global User_Input
    global User_Confirm
    global User_Story

    while User_Confirm == False: # Prevents the User from overwriting the 'Outline.txt' file
        User_Input = input("Please enter what you would like to name the file that your story will be saved to: ")
        if User_Input == "Outline":
            print("*ERROR* You cannot overwrite the 'Outline.txt' file. *ERROR*")
        else: # Stores the name of the new file once a valid entry has been entered
            File_Name = User_Input + ".txt"
            break

    # Creating the custom .txt file
    New_File = open(File_Name,"w")
    New_File.write(User_Story) # Writing the User's story to the new file
    print("Your custom story has been saved in a file called: " + File_Name)
    New_File.close()
    
    input("\nPress 'enter' to continue.")

########################################################### PROGRAM FLOW #################################################################

while Is_Running == True:

    # Clearing the screen for readability
    cls()

    print("Welcome to Mad Libs!".center(80, " "))
    print("\nPlease enter the requested information to generate your custom Mad Lib.")

    Load_File() # Loads the 'Outline.txt' file into the program
    Prompt_User() # Prompts the User to enter information to customize the MadLibs
    Display_Story() # Displays the User their customized MadLibs

    while User_Confirm == False:
        User_Input = input("\nWould you like to save your custom story to a new file? (y/n): ")
        if User_Input.upper() == "Y":
            Export_Story() # Exports the User's customized MadLibs into a new .txt file
            break
        elif User_Input.upper() == "N":
            break
        else:
            print("Please enter a valid selection.")

    Outline.close()

    while User_Confirm == False:
        User_Input = input("\nWould you like to play again? (y/n): ")
        if User_Input.upper() == "Y":
            break
        elif User_Input.upper() == "N":
            Is_Running = False
            break
        else:
            print("Please enter a valid selection.")