from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(h)]
    dist = [[-1] * w for _ in [0] * h]
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

    res = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == "." or dist[i][j] > -1:
                continue
            res += 1
            dist[i][j] = 0
            next_visit = deque([(j, i)])
            while next_visit:
                cur_x, cur_y = next_visit.popleft()
                for dir_x, dir_y in dir:
                    next_x, next_y = cur_x + dir_x, cur_y + dir_y
                    if not (0 <= next_x < w and 0 <= next_y < h):
                        continue
                    if s[next_y][next_x] == "." or dist[next_y][next_x] > -1:
                        continue
                    dist[next_y][next_x] = dist[cur_y][cur_x] + 1
                    next_visit.append((next_x, next_y))

    print(res)


if __name__ == "__main__":
    main()
