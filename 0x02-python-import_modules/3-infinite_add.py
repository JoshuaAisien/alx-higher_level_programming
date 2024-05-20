#!/usr/bin/python3
import sys
# get list of numbers
number_list = sys.argv[1:]
# new list created for addition

if __name__ == "__main__":
    augmented_list = [int(i) for i in number_list if i.isdigit()]
    sum_of_digits = sum(augmented_list)
    print()
    print(sum_of_digits)