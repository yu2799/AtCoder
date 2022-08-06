from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    res = []
    for i in list(permutations(range(1, m + 1), n)):
        prev = i[0]
        for j in i[1:]:
            if prev >= j:
                break
            prev = j
        else:
            res.append(i)
    for i in res:
        print(*i)


if __name__ == "__main__":
    main()
