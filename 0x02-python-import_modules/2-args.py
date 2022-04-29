#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print(f"0 arguments.")
    elif len(argv) == 2:
        print(f"{len(argv) - 1} argument:")
        print(f"{len(argv) - 1}: {argv[1]}")
    elif len(argv) > 2:
        print(f"{len(argv) - 1} arguments:")
        for i in range(1, len(argv)):
            print(f"{i}: {argv[i]}")
"""
n = len(sys.argv)

print(f"{n - 1} arguments.")

for i in range(1, n):
    if i < n:
        print(f"{n}:", sys.argv[i])
"""
