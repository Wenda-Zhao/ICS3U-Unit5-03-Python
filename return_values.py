#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Jan 2021
# This program for return_values


def conversion(Level_user, percentage):
    # This function is for conversion

    # process
    if Level_user == "4+":
        percentage = 98
    elif Level_user == "4":
        percentage = 90
    elif Level_user == "4-":
        percentage = 83
    elif Level_user == "3+":
        percentage = 78
    elif Level_user == "3":
        percentage = 74
    elif Level_user == "3-":
        percentage = 71
    elif Level_user == "2+":
        percentage = 68
    elif Level_user == "2":
        percentage = 65
    elif Level_user == "2-":
        percentage = 61
    elif Level_user == "1+":
        percentage = 58
    elif Level_user == "1":
        percentage = 54
    elif Level_user == "1-":
        percentage = 51
    elif Level_user == "R":
        percentage = 20

    return percentage


def main():
    # This function is for input

    percentage = -1

    # input
    Level_user = str(input("Enter the level:"))

    # call function
    percentage = conversion(Level_user, percentage)

    # output
    print("The middle percentage is:{0}% ".format(percentage))


if __name__ == "__main__":
    main()
