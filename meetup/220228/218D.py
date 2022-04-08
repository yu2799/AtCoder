from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xy = {tuple(map(int, input().split())) for _ in [0] * n}
    res = 0
    for x1, y1 in xy:
        for x2, y2 in xy:
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in xy and (x2, y1) in xy:
                res += 1
    print(res // 4)


if __name__ == "__main__":
    main()
