
2#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(argc))
        #!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    total = 0

    for i in range(1, len(argv)):
        total += int(argv[i])

    print(total)
for i in range(1, argc + 1):
            print("{}: {}".format(i, argv[i]))
