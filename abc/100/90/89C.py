from sys import stdin
from itertools import combinations


def main():
    input = stdin.readline
    n = int(input())
    c = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
    res = 0
    for _ in [0] * n:
        buf = input()[0]
        if buf in c:
            c[buf] += 1
    for i, j, k in combinations("MARCH", 3):
        res += c[i] * c[j] * c[k]
    print(res)

if __name__ == "__main__":
    main()
