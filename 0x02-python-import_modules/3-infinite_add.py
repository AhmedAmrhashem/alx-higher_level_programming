#!/usr/bin/python3
if __name__ == "__main__":
    """sum of args"""
    import sys
    count = len(sys.argv)
    sumarg = 0
    for i in range(1, count):
        sumarg += int(sys.argv[i])
    print("{}".format(sumarg))
