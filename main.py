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
        if '1' in selectedTypes:
            password.append(random.choice(characterList[0])) # Add a random lowercase letter to the password
        if '2' in selectedTypes:
            password.append(random.choice(characterList[0]).upper()) # Add a random uppercase letter to the password
        if '3' in selectedTypes:
            password.append(random.choice(characterList[1])) # Add a random special character to the password
        if '4' in selectedTypes:
            password.append(str(random.choice(characterList[2]))) # Add a random number to the password

    random.shuffle(password)  # Shuffle the characters in the password for added security
    return ''.join(password)  # Return the password as a string


# Function to get the user's choice
def getUserChoice():
    global passwordLength
    header('PASSWORD GENERATOR', bottomline = False)  # Display the header
    menu('Lowercase Letters',  # Display the menu options
         'Uppercase Letters',
         'Special Characters',
         'Numbers',
         'FINISH')

    selectedTypes = []  # List to store the types of characters chosen by the user
    options = {'1': 'Numbers',
               '2': 'Uppercase Letters',
               '3': 'Lowercase Letters',
               '4': 'Special Characters',
               '5': 'FINISH'}

    while True:
        chosenCharacter = input('ENTER THE NUMBER OF THE CHARACTER YOU WANT: ')  # Ask the user to choose a character type
        if chosenCharacter not in options:  # Check if the choice is valid
            print('INVALID OPTION! TRY AGAIN!')  # Error message for invalid choice
            continue
        elif chosenCharacter in selectedTypes:  # Check if the choice has already been selected
            print('CHARACTER TYPE ALREADY SELECTED! TRY AGAIN!')
            continue

        if chosenCharacter == '5':  # If the user chose to finish
            clearConsole()  # Clear the console

            choices = ' | '.join([options[i] for i in selectedTypes]) # Join the selected character types
            minSize = max(len(choices) + 4, 42) # Get the minimum size for the console

            header('CHOOSEN CHARACTER TYPES', bottomline = False, size = minSize)  # Display the header
            print(choices.center(minSize))  # Display the centered selected character types
            line(minSize)  # Display a line in the console

            while True:
                try:
                    passwordLength = int(input('ENTER THE PASSWORD LENGTH: '))  # Ask the user to enter the password length
                except (ValueError, TypeError):  # Check for invalid input
                    print('INVALID INPUT! TRY AGAIN!')
                    continue
                else:
                    print('LOADING', end='')  # Loading message
                    for i in range(3):
                        time.sleep(0.25)
                        print('.', end='')  # Display loading dots
                    break  # Exit the loop
            break # Exit the loop
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