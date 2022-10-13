#!/usr/bin/env python3
# Created By: Marcus Wehbi
# Date: Oct 11th, 2022
# This program asks the user for an integer
# It then displays if they number is positive, negative, or 0


def main():
    # get the users input (users integer of choice)
    user_num = int(input("Choose an integer : "))

    # check if the user selected a positive or negative integer or 0
    if user_num > 0:
        # tell the user if they entered a positive integer
        print("You entered a positive integer.")
    elif user_num < 0:
        # tell the user if they entered a negative integer
        print("You entered a negative number.")
    else:
        # tell the user they entered 0
        print("You entered 0.")


if __name__ == "__main__":
    main()
