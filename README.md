# Random Password Generator

## Introduction

This Python script generates strong, random passwords based on user-specified length. It aims to create passwords that are difficult to guess by incorporating a mix of character types.

## How it Works

1.  **User Input**: The script prompts the user to enter the desired length for the password.
2.  **Character Mix**: It constructs the password using a combination of:
    *   Lowercase letters (`a-z`)
    *   Uppercase letters (`A-Z`)
    *   Digits (`0-9`)
    *   Special characters (e.g., `!@#$%^&*()`)
3.  **Strength Assurance**: If the specified password length is sufficient (e.g., 4 characters or more), the script ensures that at least one character from each of the above categories is included. This significantly increases the password's strength. For shorter lengths, it uses a subset of character types.
4.  **Randomization**: The final set of characters is then shuffled randomly to produce the final password.

## Features

*   **Customizable Length**: Users can specify the exact length of the password they need.
*   **Character Variety**: Generates passwords with a mix of lowercase, uppercase, digits, and special characters.
*   **Strength Focus**: Prioritizes including all character types for robust passwords (length permitting).
*   **User-Friendly**: Simple command-line interaction.

## How to Run

1.  Ensure you have Python installed on your system.
2.  Save the script as `Password.py` (or the name you have chosen).
3.  Open a terminal or command prompt.
4.  Navigate to the directory where you saved the script.
5.  Run the script using the following command:

    ```bash
    python Password.py
    ```
6.  Follow the on-screen prompts to enter the desired password length and generate passwords.

---
This script provides a straightforward way to generate secure passwords for various online accounts and security needs.
