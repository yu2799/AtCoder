from sys import stdin
from itertools import permutations


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    t = [[int(i) for i in input().split()] for _ in [0] * n]
    permutation = list(permutations(range(n)))
    res = 0
    for i in permutation:
        if i[0] == 0:
            tmp = 0
            prev = 0
            for j in i[1:]:
                tmp += t[prev][j]
                prev = j
            else:
                tmp += t[prev][0]
                if tmp == k:
                    res += 1
        else:
            print(res)
            break


if __name__ == "__main__":
    main()
