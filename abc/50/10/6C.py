from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    for y in [0, 1]:
        x = (4 * n - m - y) // 2
        z = n - x - y
        if x >= 0 and z >= 0 and 2 * x + 3 * y + 4 * z == m:
            print(x, y, z)
            return
    print(-1, -1, -1)


if __name__ == "__main__":
    main()
