from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    dir = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    res = []
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        grid = (
            [list("0" * (w + 2))]
            + [list("0") + list(input().split()) + list("0") for _ in [0] * h]
            + [list("0" * (w + 2))]
        )
        tmp = 0
        visited = set()
        for i in range(1, h + 1):
            for j in range(1, w + 1):
                if grid[i][j] == "1" and (i, j) not in visited:
                    next_visited = deque([(i, j)])
                    while next_visited:
                        cur_y, cur_x = next_visited.pop()
                        visited.add((cur_y, cur_x))
                        for dir_i, dir_j in dir:
                            next_x = cur_x + dir_i
                            next_y = cur_y + dir_j
                            if (next_y, next_x) in visited:
                                continue
                            if grid[next_y][next_x] == "1":
                                next_visited.append((next_y, next_x))
                    tmp += 1
        res.append(tmp)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
