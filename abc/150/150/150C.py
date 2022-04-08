from sys import stdin
from itertools import permutations


def main():
    input = stdin.readline
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    permutation = list(permutations(list(range(1, n + 1))))
    print(abs(permutation.index(p) - permutation.index(q)))


if __name__ == "__main__":
    main()
