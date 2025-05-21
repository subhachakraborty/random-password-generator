import random
import sys
import string

# Character sets for password generation
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

def generate_password(password_length: int) -> str:
    """Generates a strong random password with a mix of character types."""

    if password_length <= 0:
        return "Password length must be greater than 0."
    if password_length > 1000: # Arbitrary upper limit to prevent performance issues
        return "Password length is too large."

    # Ensure at least one of each character type if length allows
    char_types = [lowercase_letters, uppercase_letters, digits, special_characters]
    
    # Handle cases where password_length is less than the number of character types
    if password_length < len(char_types):
        # Use a subset of character types or repeat characters from fewer types
        selected_types = char_types[:password_length]
        password_chars_list = []
        for i in range(password_length):
            password_chars_list.extend(random.choices(selected_types[i % len(selected_types)], k=1))
    else:
        # Guaranteed one of each type
        num_lowercase = 1
        num_uppercase = 1
        num_digits = 1
        num_special = 1

        # Remaining length to distribute
        remaining_length = password_length - (num_lowercase + num_uppercase + num_digits + num_special)

        # Distribute remaining length randomly among the four types
        # This is a simplified distribution. A more complex one could ensure better randomness.
        for _ in range(remaining_length):
            choice = random.randint(0, 3)
            if choice == 0:
                num_lowercase += 1
            elif choice == 1:
                num_uppercase += 1
            elif choice == 2:
                num_digits += 1
            else:
                num_special += 1
        
        # Select characters for each type
        lowercase_sample = random.choices(lowercase_letters, k=num_lowercase)
        uppercase_sample = random.choices(uppercase_letters, k=num_uppercase)
        digits_sample = random.choices(digits, k=num_digits)
        special_sample = random.choices(special_characters, k=num_special)

        # Combine all characters
        password_chars_list = lowercase_sample + uppercase_sample + digits_sample + special_sample

    # Shuffle the combined list of characters to ensure randomness
    random.shuffle(password_chars_list)

    # Convert the list of characters to a string
    generated_password = "".join(password_chars_list)
    return generated_password

def main():
    """Handles user interaction for password generation."""
    while True:
        try:
            password_length_str = input("Enter the desired password length (e.g., 12): ")
            if not password_length_str: # Handle empty input
                print("No input provided for password length.")
                continue
            password_length = int(password_length_str)
        except ValueError:
            print("Invalid input. Please enter a number for the password length.")
            continue

        if password_length <= 0:
            print("Password length must be a positive number.")
            continue
        
        # Generate the password
        new_password = generate_password(password_length)
        print(f"Generated Password: {new_password}")

        # Ask user if they want to generate another password
        user_command = input("Type 'again' to generate another password, or anything else to quit: ").lower()
        if user_command != "again":
            break
    
    print("Thank you for using the password generator. Have a nice day!")
    sys.exit()

if __name__ == "__main__":
    main()
