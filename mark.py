#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program calculates a user input level into a percentage


def level_convert(user_level):
    # calculates level to a percentage

    # process
    if user_level == "4+":
        grade_per = 97.5
    elif user_level == "4":
        grade_per = 90.5
    elif user_level == "4-":
        grade_per = 83
    elif user_level == "3+":
        grade_per = 78
    elif user_level == "3":
        grade_per = 74.5
    elif user_level == "3-":
        grade_per = 71
    elif user_level == "2+":
        grade_per = 68
    elif user_level == "2":
        grade_per = 64.5
    elif user_level == "2-":
        grade_per = 61
    elif user_level == "1+":
        grade_per = 58
    elif user_level == "1":
        grade_per = 54.5
    elif user_level == "1-":
        grade_per = 51
    elif user_level == "R":
        grade_per = 24.5
    elif user_level != "":
        grade_per = -1
    return grade_per


def main():
    # this function just calls other functions

    # input
    user_level = input("Enter the level you want to convert to a percentage: ")
    print("")

    # call function
    level_converted = level_convert(user_level)

    print("Level {0} has a middle percentage of {1}%".format(user_level, level_converted))
    print("\nDone.")


if __name__ == "__main__":
    main()
