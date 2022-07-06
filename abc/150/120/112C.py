from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    xyh = [tuple(map(int, input().split())) for _ in [0] * n]
    for x, y, h in xyh:
        if h != 0:
            px, py, ph = x, y, h
            break

    for xi in range(101):
        for yi in range(101):
            hi = ph + abs(px - xi) + abs(py - yi)
            for x, y, h in xyh:
                tmp = max(hi - abs(x - xi) - abs(y - yi), 0)
                if h != tmp:
                    break
            else:
                print(xi, yi, hi)


if __name__ == "__main__":
    main()
