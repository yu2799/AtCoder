from sys import stdin


def main():
    input = stdin.readline
    n, k = map(int, input().split())
    s = input()[:-1]
    res = 0
    prev = s[0]
    for i in s[1:]:
        if prev == i:
            res += 1
        else:
            prev = i
    res += min(n - res - 1, k * 2)
    print(res)


if __name__ == "__main__":
    main()
