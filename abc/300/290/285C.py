from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    res = 0
    cnt = 0
    for i in reversed(s):
        res += (ord(i) - 64) * pow(26, cnt)
        cnt += 1
    print(res)


if __name__ == "__main__":
    main()
