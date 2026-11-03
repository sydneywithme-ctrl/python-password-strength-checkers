import string 
import getpass

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for uppercase letters
    if not any(char.isupper() for char in password):
        return "Weak: Password must contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not any(char.islower() for char in password):
        return "Weak: Password must contain at least one lowercase letter."
    
    # Check for digits
    if not any(char.isdigit() for char in password):
        return "Weak: Password must contain at least one digit."
    
    # Check for special characters
    special_characters = string.punctuation
    if not any(char in special_characters for char in password):
        return "Weak: Password must contain at least one special character."
    
    return "Strong: Your password is strong."

def main():
    password = getpass.getpass("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

if __name__ == "__main__":
    main()

print("Password Strength Checker")

