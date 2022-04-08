from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    h = int(input())
    print(sqrt(h * (12800000 + h)))


if __name__ == "__main__":
    main()
