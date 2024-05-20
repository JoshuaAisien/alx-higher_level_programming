import sys
arg_list = sys.argv

counter = 0
for i in arg_list:
    if i == "fast":
        print(f"{arg_list[counter]} at position {counter}")
        break
    counter += 1