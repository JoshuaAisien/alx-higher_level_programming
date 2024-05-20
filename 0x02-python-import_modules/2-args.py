#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_list = sys.argv
    print(f"{len(arg_list) - 1} arguments")
    arg_list.pop(0)
    count = 0
    for i in arg_list:
        count += 1
        print(f"{count}: {i}")

