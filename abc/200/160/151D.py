from sys import stdin
from collections import deque


def grid_bfs(grid, w, h, x, y):
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
        [["#"] * (w + 2)]
        + [list("#" + input()[:-1] + "#") for _ in [0] * h]
        + [["#"] * (w + 2)]
    )
    res = 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i][j] == ".":
                tmp = max([max(i) for i in grid_bfs(grid, w + 2, h + 2, j, i)])
                if res < tmp:
                    res = tmp
    print(res)


if __name__ == "__main__":
    main()
