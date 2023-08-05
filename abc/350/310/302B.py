from sys import stdin


def solve(s, y, x, h, w):
    buf = "snuke"
    dir = [
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ]
    for dx, dy in dir:
        cnt = 0
        cur_x = x
        cur_y = y
        while (
            cnt < 5
            and 0 <= cur_y < h
            and 0 <= cur_x < w
            and buf[cnt] == s[cur_y][cur_x]
        ):
            cur_x += dx
            cur_y += dy
            cnt += 1
        if cnt == 5:
            for i in range(5):
                print(1 + y + dy * i, 1 + x + dx * i)
            return True
    return False


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] == "s" and solve(s, i, j, h, w):
                return


if __name__ == "__main__":
    main()
