#!/usr/bin/python3
if __name__ == "__main__":
    import sys

sum1 = 0
i = 1
while(len(sys.argv) - 1 >= i):
    sum1 += int(sys.argv[i])
    i += 1
print("{}".format(sum1))
