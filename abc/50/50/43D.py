from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    n = len(s)
    for i in range(n):
        if i + 1 < n and s[i] == s[i + 1]:
            print(i + 1, i + 2)
            return
        if i + 2 < n and s[i] == s[i + 2]:
            print(i + 1, i + 3)
            return
    print(-1, -1)


if __name__ == "__main__":
    main()
