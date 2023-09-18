from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    n = list(input()[:-1])
    len_n = len(n)
    res = 0
    for i in permutations(n):
        for j in range(1, len_n):
            if i[0] == 0 or i[j] == 0:
                continue
            tmp = int("".join(i[:j])) * int("".join(i[j:]))
            res = max(res, tmp)
    print(res)


if __name__ == "__main__":
    main()
