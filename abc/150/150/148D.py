from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    cnt = 1
    for i in a:
        if i != cnt:
            res += 1
        else:
            cnt += 1
    print(-1 if res == n else res)


if __name__ == "__main__":
    main()
