from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    res = 0
    if 1 < r:
        res += 1
    if r < h:
        res += 1
    if 1 < c:
        res += 1
    if c < w:
        res += 1
    print(res)


if __name__ == '__main__':
    main()
