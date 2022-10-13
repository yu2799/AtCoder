from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(map(int, input().split()))
    res = 0
    for idx, i in enumerate(a):
        if (idx + 1) % 2 and i % 2:
            res += 1
    print(res)


if __name__ == "__main__":
    main()
