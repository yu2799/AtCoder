from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    snuke = {
        "s": 0,
        "n": 1,
        "u": 2,
        "k": 3,
        "e": 4,
    }
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [(0, 0)]
    visited = set()
    while stack:
        cur_y, cur_x = stack.pop()
        if cur_y == h - 1 and cur_x == w - 1:
            print("Yes")
            return
        cur_buf = s[cur_y][cur_x]
        visited.add((cur_y, cur_x))
        for y, x in dir:
            next_y = cur_y + y
            next_x = cur_x + x
            if not (0 <= next_y < h and 0 <= next_x < w):
                continue
            next_buf = s[next_y][next_x]
            if (
                next_buf in snuke
                and snuke[next_buf] == (snuke[cur_buf] + 1) % 5
                and (next_y, next_x) not in visited
            ):
                stack.append((next_y, next_x))
    print("No")


if __name__ == "__main__":
    main()
