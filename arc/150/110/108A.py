from sys import stdin
from math import sqrt


def main():
    input = stdin.readline
    s, p = map(int, input().split())
    for i in range(1, int(sqrt(p)) + 1):
        if i * (s - i) == p:
            print("Yes")
            return
    print("No")


if __name__ == '__main__':
    main()
