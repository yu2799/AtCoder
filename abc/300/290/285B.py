from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    res = []
    for i in range(1, n):
        l = 0
        while l + i < n and s[l] != s[l + i]:
            l += 1
        res.append(l)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
