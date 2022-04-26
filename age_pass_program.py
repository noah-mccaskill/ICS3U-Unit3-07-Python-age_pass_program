# /usr/bin/env python3

# Created by: Noah McCaskill
# Created on: April 2022
# This program asks the user's age for dating permission


def main():
    # this function checks if the user follows the age guidelines for dating

    # input
    age = input("What is your age?: ")
    print("")

    # process & output
    try:
        integer_as_number = int(age)

        if integer_as_number >= 25 and integer_as_number <= 40:
            print("You are allowed to date.")

        else:
            print("You are not eligible to date.")

    except Exception:
        print("You entered an invalid answer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
