from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    h = list(map(int, input().split()))
    res = 0
    tmp = 0
    for i in h:
        if tmp <= i:
            tmp = i
            res += 1
    print(res)


if __name__ == "__main__":
    main()
