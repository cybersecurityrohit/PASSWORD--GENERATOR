import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length for the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
