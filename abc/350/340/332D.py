from itertools import permutations
from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    ph = list(permutations(list(range(h))))
    pw = list(permutations(list(range(w))))
    print(ph)


if __name__ == "__main__":
    main()
