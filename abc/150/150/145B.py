from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    print("Yes" if s[: n // 2] == s[n // 2 :] else "No")


if __name__ == "__main__":
    main()
