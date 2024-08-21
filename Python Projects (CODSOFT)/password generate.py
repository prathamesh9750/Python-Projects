import random
import string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Define character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure the password includes at least one character from each set
    all_characters = lower_case + upper_case + digits + special_chars
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random characters
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Example usage
if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(length))
