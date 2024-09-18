# Password Generator

This project is a simple password generator tool. It allows users to generate passwords based on their preferences, including options for lowercase letters, uppercase letters, special characters, and numbers.

## Files

### `main.py`

Contains the main functionality of the password generator:
- **`generatePassword(selectedTypes, passwordLength)`**: Generates a random password based on selected character types and length.
- **`getUserChoice()`**: Prompts the user to select character types and password length.
- **`getPassword()`**: Calls `getUserChoice()` to get user preferences and generates the password.

### `interface.py`

Provides utility functions for formatting the terminal:
- **`line(size = 42)`**: Prints a line of equal signs (`=`) with a default size of 42 characters.
- **`menu(*options, topline = True, bottomline = True, size = 42)`**: Prints a menu with numbered options, with optional top and bottom lines.
- **`header(title, topline = True, bottomline = True, size = 42)`**: Prints a centered header with optional top and bottom lines.
- **`clearConsole(cooldown = 1)`**: Clears the console screen after a specified delay.

## How to Use

1. **Run the Application:**
   - Execute `main.py` to start the password generator.

2. **Select Character Types:**
   - Follow the prompts to choose the types of characters you want in your password (lowercase letters, uppercase letters, special characters, numbers).

3. **Set Password Length:**
   - Enter the desired length for the password when prompted.

4. **View Generated Password:**
   - The application will display the generated password based on your selections.

## Installation

Clone the repository:
```bash
git clone https://github.com/lcsvme/pythonPasswordGenerator.git
```

## Contributions

Contributions are welcome! If you have improvements or suggestions, feel free to open an issue or submit a pull request.

## Credits

Made with love by [Luan Vieira](https://github.com/lcsvme). Check out my other projects on GitHub!
