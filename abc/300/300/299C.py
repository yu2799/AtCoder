from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    cnt = 0
    res = 0
    for i in range(n):
        if s[i] == "o":
            cnt += 1
        else:
            if res < cnt:
                res = cnt
            cnt = 0

    cnt = 0
    for i in range(n - 1, -1, -1):
        if s[i] == "o":
            cnt += 1
        else:
            if res < cnt:
                res = cnt
            cnt = 0
    print(res if res != 0 else -1)


if __name__ == "__main__":
    main()
