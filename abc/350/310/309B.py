from copy import deepcopy
from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [list(input()[:-1]) for _ in range(n)]
    b = deepcopy(a)
    for i in range(n - 1):
        b[0][i + 1] = a[0][i]
    for i in range(n - 1):
        b[i + 1][n - 1] = a[i][n - 1]
    for i in range(n - 1, 0, -1):
        b[n - 1][i - 1] = a[n - 1][i]
    for i in range(n - 1, 0, -1):
        b[i - 1][0] = a[i][0]
    for i in b:
        print("".join(i))


if __name__ == "__main__":
    main()
