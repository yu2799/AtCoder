from sys import stdin


def main():
    input = stdin.readline
    _, d, k = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in [0] * d]
    res = []
    for _ in [0] * k:
        s, t = map(int, input().split())
        cur = s
        for idx, (left, right) in enumerate(lr):
            if left <= cur <= right:
                cur = right if s < t else left
            if s < t:
                if t <= cur:
                    res.append(idx + 1)
                    break
            else:
                if cur <= t:
                    res.append(idx + 1)
                    break
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
