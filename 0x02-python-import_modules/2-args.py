#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments."""

    import sys

    counter = len(sys.argv)
    if counter == 1:
        print("0 arguments.")
    else:
        print("{} arguments:" .format(counter - 1))
        for i in range(1, counter):
            print("{} : {}" .format(i, sys.argv[i]))