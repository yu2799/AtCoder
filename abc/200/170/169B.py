from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = [int(i) for i in input().split()]
    if 0 in a:
        print(0)
        exit()
    res = 1
    for i in a:
        res = res * i
        if res > 1000000000000000000:
            print(-1)
            exit()
    print(res)


if __name__ == "__main__":
    main()
