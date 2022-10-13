from collections import deque
from sys import stdin


def get_dir(n, m):
    dir = []
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if x == 0 and n < abs(y):
                continue
            if y == 0 and n < abs(x):
                continue
            if m == x * x + y * y:
                dir.append((x, y))
    return dir


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    dist = [[-1] * n for _ in [0] * n]
    dist[0][0] = 0
    dir = get_dir(n, m)
    next_visit = deque([(0, 0)])
    while next_visit:
        cur_x, cur_y = next_visit.popleft()
        for dir_x, dir_y in dir:
            next_x, next_y = cur_x + dir_x, cur_y + dir_y
            if (
                0 <= next_x < n
                and 0 <= next_y < n
                and dist[next_y][next_x] == -1
            ):
                dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                next_visit.append((next_x, next_y))
    for i in dist:
        print(*i)


if __name__ == "__main__":
    main()
