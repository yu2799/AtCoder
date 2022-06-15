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
    r, c = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())
    grid = [list(input()[:-1]) for _ in [0] * r]
    dist = grid_bfs(grid, c, r, sx, sy)
    print(dist[gy][gx])


if __name__ == "__main__":
    main()
