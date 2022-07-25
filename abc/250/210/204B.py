from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in a:
        if i >= 10:
            res = res + i - 10
    print(res)


if __name__ == "__main__":
    main()
