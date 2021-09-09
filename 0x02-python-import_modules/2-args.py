#!/usr/bin/python3

if __name__ == "__main__":
    import sys

if (len(sys.argv) - 1) == 0:
    print("0 arguments.")
elif (len(sys.argv) - 1) == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(len(sys.argv) - 1))
if len(sys.argv) - 1 >= 1:
    i = 1
    while(len(sys.argv) - 1 >= i):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
