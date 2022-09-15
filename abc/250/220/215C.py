from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    s, k = input().split()
    k = int(k) - 1
    print(*sorted(set(permutations(s)))[k], sep="")


if __name__ == "__main__":
    main()
