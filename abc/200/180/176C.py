from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = 0
    tmp = 0
    for i in a:
        if tmp < i:
            tmp = i

        res += tmp - i
    print(res)


if __name__ == "__main__":
    main()
