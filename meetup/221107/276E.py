from collections import deque
from sys import stdin


def grid_bfs(grid, w, h, x, y, sx, sy):
    dist = [[-1] * w for _ in [0] * h]
    dist[y][x] = 0
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    next_visit = deque([(x, y)])
    while next_visit:
        cur_x, cur_y = next_visit.popleft()
        for dir_x, dir_y in dir:
            next_x, next_y = cur_x + dir_x, cur_y + dir_y
            if (
                grid[next_y][next_x] == "#"
                or grid[next_y][next_x] == "S"
                or dist[next_y][next_x] > -1
            ):
                continue
            dist[next_y][next_x] = dist[cur_y][cur_x] + 1
            next_visit.append((next_x, next_y))
    for dir_x, dir_y in dir:
        if dist[sy + dir_y][sx + dir_x] > 0:
            return True
    return False


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    grid = (
        [list("#" * (w + 2))]
        + [list("#") + list(input()[:-1]) + list("#") for _ in [0] * h]
        + [list("#" * (w + 2))]
    )
    sx, sy = 0, 0
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i][j] == "S":
                sx = j
                sy = i
                break
        else:
            continue
        break

    for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        dir_x += sx
        dir_y += sy
        if grid[dir_y][dir_x] == "." and grid_bfs(
            grid, w + 2, h + 2, dir_x, dir_y, sx, sy
        ):
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
