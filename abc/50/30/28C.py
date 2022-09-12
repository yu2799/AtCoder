from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    a = list(map(int, input().split()))
    tmp = list(set(sum(i) for i in permutations(a, 3)))
    tmp.sort(reverse=True)
    print(tmp[2])


if __name__ == "__main__":
    main()
