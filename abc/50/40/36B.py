from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [list(input()[:-1]) for _ in [0] * n]
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(s[j][i], end="")
        print("")


if __name__ == "__main__":
    main()
