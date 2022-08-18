from collections import Counter
from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    tmp = []
    for i, j in Counter(s).items():
        for _ in [0] * min(j, 3):
            tmp.append(i)
    for i in permutations(tmp, min(3, len(s))):
        if int("".join(i)) % 8 == 0:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
