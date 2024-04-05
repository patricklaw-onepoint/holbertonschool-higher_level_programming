#!/usr/bin/python3
def print_arg(argv):
    n = len(argv)-1
    match n:
        case 0:
            print("0 arguments.")
        case 1:
            print("{} argument:".format(n))
            print("1: {}".format(argv[1]))
        case _:
            print("{} arguments:".format(n))
            for i in range(1, n + 1):
                print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
