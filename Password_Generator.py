import random
import string

def generate_password( length, complexity):
    if complexity == 1:
        characters = string.ascii_uppercase
    elif complexity == 2:
        characters = string.ascii_lowercase
    elif complexity == 3:
        characters = string.digits
    elif complexity == 4:
        characters = string.punctuation
    else:
        raise ValueError("Complexity must be between 1 and 4")
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        print("Select complexity level:")
        print("1: Uppercase letters")
        print("2: Lowercase letters")
        print("3: Digits")
        print("4: Special characters")
        complexity = int(input("Enter the complexity level (1-4): "))
        
        if length <= 0:
            raise ValueError("Length must be a positive integer")
        
        password = generate_password(length, complexity)
        print(f"Generated password: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()