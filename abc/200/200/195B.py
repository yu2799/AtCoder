from sys import stdin
from math import floor, ceil


def main():
    input = stdin.readline
    a, b, w = map(int, input().split())
    upper = int(floor(1000 * w / a))
    lower = int(ceil(1000 * w / b))
    if lower > upper:
        print("UNSATISFIABLE")
    else:
        print(lower, upper)


if __name__ == "__main__":
    main()
