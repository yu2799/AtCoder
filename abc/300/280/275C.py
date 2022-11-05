from sys import stdin


def check(x, y, s):
    res = 0
    for i in range(-8, 9):
        ty = y + i
        for j in range(-8, 9):
            if i == 0 and j == 0:
                continue
            tx = x + j
            if 0 <= ty <= 8 and 0 <= tx <= 8 and s[ty][tx] == "#":
                sy = y - j
                sx = x + i

                if (
                    0 <= sy <= 8
                    and 0 <= sx <= 8
                    and s[sy][sx] == "#"
                    and 0 <= ty - j <= 8
                    and 0 <= tx + i <= 8
                    and s[ty - j][tx + i] == "#"
                ):
                    res += 1
    return res


def main():
    input = stdin.readline
    s = [list(input()[:-1]) for _ in [0] * 9]
    res = 0
    for x in range(9):
        for y in range(9):
            if s[y][x] == "#":
                res += check(x, y, s)
    print(res // 4)


if __name__ == "__main__":
    main()
