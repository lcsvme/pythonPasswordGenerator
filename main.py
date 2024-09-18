import random
import time
from interface import *


# Function to generate a random password
def generatePassword(selectedTypes, passwordLength):
    password = []  # List to store the password
    characterList = [  # List of character types
        ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],  # Lowercase letters
        ['!', '@', '#', '$', '%', '&', '*', '+', '=', '?'],  # Special characters
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]  # Numbers
    ]

    # Loop to generate the password based on the user's choice and password size
    while len(password) < int(passwordLength):
        if '1' in selectedTypes:  # If the user chose numbers
            password.append(str(random.choice(characterList[2])))  # Add a number to the password
        if '2' in selectedTypes:  # If the user chose uppercase letters
            password.append(random.choice(characterList[0]).upper())  # Add an uppercase letter to the password
        if '3' in selectedTypes:  # If the user chose lowercase letters
            password.append(str(random.choice(characterList[0])))  # Add a lowercase letter to the password
        if '4' in selectedTypes:  # If the user chose special characters
            password.append(random.choice(characterList[1]))  # Add a special character to the password

    random.shuffle(password)  # Shuffle the characters in the password for added security

    return ''.join(password)  # Return the password as a string


# Function to get the user's choice
def getUserChoice():
    header('PASSWORD GENERATOR')  # Display the header
    menu('Numbers',  # Display the menu options
         'Uppercase Letters',
         'Lowercase Letters',
         'Special Characters',
         'FINISH')

    selectedTypes = []  # List to store the types of characters chosen by the user
    options = {'1': 'Numbers', '2': 'Uppercase Letters', '3': 'Lowercase Letters', '4': 'Special Characters',
               '5': 'FINISH'}

    while True:
        chosenCharacter = input(
            'ENTER THE NUMBER OF THE CHARACTER YOU WANT: ')  # Ask the user to choose a character type
        if chosenCharacter not in options:  # Check if the choice is valid
            print('INVALID OPTION! TRY AGAIN!')  # Error message for invalid choice
            clearConsole(0.75)  # Clear the console after 0.75 seconds
            continue

        if chosenCharacter == '5':  # If the user chose to finish
            line()  # Display a line in the console
            passwordLength = input('ENTER THE PASSWORD LENGTH: ')  # Ask the user to enter the password length
            print('LOADING', end='')  # Loading message
            for i in range(3):
                time.sleep(0.45)
                print('.', end='')  # Display loading dots
            break  # Exit the loop
        else:
            selectedTypes.append(chosenCharacter)  # Add the user's choice to the list

    return selectedTypes, passwordLength  # Return the selected character types and the password length


# Main function to generate the password
def getPassword():
    selectedTypes, passwordLength = getUserChoice()  # Get the user's choice
    password = generatePassword(selectedTypes, passwordLength)  # Generate the password based on the user's choice

    clearConsole()  # Clear the console
    line()  # Display a line in the console
    print('RANDOMLY GENERATED PASSWORD'.center(42))  # Display a centered message
    print(f'{password}'.center(42))  # Display the centered password
    line()  # Display a line in the console


if __name__ == "__main__":
    getPassword()  # Call the main function to generate the password if the script is run directly
