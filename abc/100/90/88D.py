from sys import stdin
from collections import deque


def grid_bfs(grid, h, w, x, y):
    dist = [[-1] * w for _ in [0] * h]
    dist[y][x] = 0
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    next_visit = deque([(x, y)])
    while next_visit:
        cur_x, cur_y = next_visit.popleft()
        for dir_x, dir_y in dir:
            next_x, next_y = cur_x + dir_x, cur_y + dir_y
            if grid[next_y][next_x] == "#" or dist[next_y][next_x] > -1:
                continue
            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            next_visit.append((next_x, next_y))

    return dist


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    grid = (
        [list("#" * (w + 2))]
        + [list("#") + list(input()[:-1]) + list("#") for _ in [0] * h]
        + [list("#" * (w + 2))]
    )
    res = -1
    for i in grid:
        res = res + i.count(".")
    tmp = grid_bfs(grid, h + 2, w + 2, 1, 1)[h][w]
    print(res - tmp if tmp != -1 else -1)


if __name__ == "__main__":
    main()
