from sys import stdin
from itertools import permutations


def main():
    input = stdin.readline
    s = input()[:-1]
    print(len(set(permutations(s))))


if __name__ == "__main__":
    main()
