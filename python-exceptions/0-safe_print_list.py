#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for index, value in enumerate(my_list):
        if index >= x:
            break
        try:
            print("{}".format(value), end="")
        except Exception:
            break
        else:
            count += 1
    print()
    return count
