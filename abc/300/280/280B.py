from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = list(map(int, input().split()))
    res = []
    prev = 0
    for i in s:
        res.append(i - prev)
        prev = i
    print(*res)


if __name__ == "__main__":
    main()
