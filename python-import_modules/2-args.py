#!/usr/bin/python3
def print_arg(argv):
    n = len(argv)
    match n:
        case 0:
            print("0 arguments.")
        case 1:
            print("{} argument:".format(n))
            print("{}: {}".format(1, argv[0]))
        case _:
            print("{} arguments:".format(n))
            for i in range(1, n + 1):
                print("{}: {}".format(i, argv[i]))


if __name__ == "__main__":
    import sys

    print_arg([sys.argv])
