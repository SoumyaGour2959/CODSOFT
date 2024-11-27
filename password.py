import random
import string

def generate_password():
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired length of the password (minimum 6): "))
        if length < 6:
            print("Password length must be at least 6 characters.")
            return
        
        # Define the character pools
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation
        
        # Combine all character types
        all_characters = lower_case + upper_case + digits + special_characters
        
        # Ensure the password contains at least one character from each category
        password = [
            random.choice(lower_case),
            random.choice(upper_case),
            random.choice(digits),
            random.choice(special_characters)
        ]
        
        # Fill the rest of the password length with random choices
        password += random.choices(all_characters, k=length - 4)
        
        # Shuffle the list to avoid predictable patterns
        random.shuffle(password)
        
        # Join the list into a string to form the final password
        final_password = ''.join(password)
        
        # Display the generated password
        print(f"Generated Password: {final_password}")
    
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")

# Call the function to generate the password
generate_password()
