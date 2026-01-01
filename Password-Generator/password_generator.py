import random
import string


def generate_password():

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

        include_symbols = input("Include symbols? (y/n): ").strip().lower()

        characters = string.ascii_letters + string.digits

        if include_symbols == "y":
            characters += string.punctuation

        password = ""
        for _ in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Please enter a valid number for length.")


def main():
    print("\n--- Password Generator ---")
    generate_password()


if __name__ == "__main__":
    main()