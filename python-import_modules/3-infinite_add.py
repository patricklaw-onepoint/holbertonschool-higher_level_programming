#!/usr/bin/python3
def add_args(argv):
    numbers = argv[1:]
    total = sum(int(num) for num in numbers)
    print("{:d}".format(total))

if __name__ == "__main__":
    import sys
    add_args(sys.argv)