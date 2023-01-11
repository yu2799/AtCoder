from sys import stdin


def main():
    input = stdin.readline
    t = int(input())
    res = []
    for _ in [0] * t:
        _ = int(input())
        a = list(map(int, input().split()))
        cnt = 0
        for i in a:
            if i % 2:
                cnt += 1
        res.append(cnt)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
