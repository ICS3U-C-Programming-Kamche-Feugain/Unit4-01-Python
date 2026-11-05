#!/usr/bin/env python3\
# Created By:Kamche
# Created on: November 5, 2026
# This program asks the user for numbers
# to make a while loop program
# make the users number false.


def main():
    # this function uses a while loop
    loop_counter = 0

    # this function checks if the number is a positive number
    # ask the user for a positive number
    positive_number_str = input("Enter a positive number: ")
    print("{positive_number}".format(positive_number=positive_number_str))

    # check if the positive number is valid
    try:

        positive_number_as_int = int(positive_number_str)

        if positive_number_as_int <= 0:
            print(
                "{positive_number} is not a positive number, please enter a positive number".format(
                    positive_number=positive_number_as_int
                )
            )
        else:
            sum_of_numbers = 0

            # Loop through the numbers from 0 to the user's number
            while loop_counter <= positive_number_as_int:

                print("Tracking {} times through the loop.".format(loop_counter))
                sum_of_numbers += loop_counter
                loop_counter += 1
            print(
                "The sum of all the numbers from 0 to {positive_number} is {sum_of_numbers}".format(
                    positive_number=positive_number_as_int,
                    sum_of_numbers=sum_of_numbers,
                )
            )
    except Exception:
        print(
            "{positive_number} is not a positive integer, enter a valid integer".format(
                positive_number=positive_number_str
            )
        )


if __name__ == "__main__":
    main()
