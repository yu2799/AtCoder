from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    for i in a:
        if i == 0:
            print(0)
            return
    res = 1
    for i in a:
        res *= i
        if 10**18 < res:
            print(-1)
            return
    print(res)


if __name__ == "__main__":
    main()
