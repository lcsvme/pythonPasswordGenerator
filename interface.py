def info():
    """
    Creator: Luan Vieira
    Date: 17/09/2024
    Description: This file contains functions to format the terminal. """

    print(help(info))

# Prints a line with a default size of 42 characters
def line(size = 42):
    print('=' * size)


# Prints a menu with the options passed as arguments, each option is numbered
def menu(*options, topline = True, bottomline = True, size = 42):
    if topline: # If topline is True, print a line
        line(size)

    # Print the options with their respective numbers
    for i, option in enumerate(options):
        print(f'[{i+1}]. {option}')

    if bottomline: # If bottomline is True, print a line
        line(size)


# Prints a header with the title passed as argument, centered and with a default size of 42 characters
def header(title, topline = True, bottomline = True, size = 42):
    if topline: # If topline is True, print a line
        line(size)

    # Print the title centered
    print(title.center(size))

    if bottomline: # If bottomline is True, print a line
        line(size)


# Clears the console after the time passed as argument
def clearConsole(cooldown = 1):
    import os
    import time

    time.sleep(cooldown) # Wait for the time passed as argument
    # If your IDE doesn't support the clear command, the console will be cleaned by printing 50 blank lines
    for i in range(50):
        print()

    # If your IDE supports the clear command, it will be used
    if os.name == 'nt': # If the OS is Windows
        os.system('cls')
    else: # If the OS is Linux or MacOS
        os.system('clear')

if __name__ == '__main__':
    info()