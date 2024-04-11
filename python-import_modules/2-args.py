#!/usr/bin/python3
def print_args(argv):
    n = len(argv) - 1
    if n == 0:
        print("0 arguments.")
    elif n == 1:
        print("{} argument:".format(n))
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(n))
        for i in range(1, n + 1):
            print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    import sys

    print_args(sys.argv)
