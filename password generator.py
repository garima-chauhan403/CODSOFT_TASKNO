import random
import string

print("=" * 40)
print("      PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length should be at least 4.\n")
            continue

        use_upper = input("Include Uppercase letters? (y/n): ").lower()
        use_lower = input("Include Lowercase letters? (y/n): ").lower()
        use_digits = input("Include Numbers? (y/n): ").lower()
        use_symbols = input("Include Special Characters? (y/n): ").lower()

        characters = ""

        if use_upper == "y":
            characters += string.ascii_uppercase

        if use_lower == "y":
            characters += string.ascii_lowercase

        if use_digits == "y":
            characters += string.digits

        if use_symbols == "y":
            characters += string.punctuation

        if characters == "":
            print("\nPlease select at least one character type.\n")
            continue

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print("-" * 25)
        print(password)
        print("-" * 25)

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != "y":
            print("\nThank you for using Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.\n")