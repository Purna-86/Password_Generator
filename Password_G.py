import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    length = max(length, 10)

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("\nPassword Generator")
    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)
    print("Generating...")
    print("Generated Password:", password)
    print("Successfully Completed!!!")
if __name__ == "__main__":
    main()

