from collections import deque
from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    s = [list(input()[:-1]) for _ in range(n)]
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q = deque([(1, 1)])
    visited = set()
    passed = set()
    while q:
        cur_y, cur_x = q.popleft()
        visited.add((cur_y, cur_x))
        passed.add((cur_y, cur_x))
        for x, y in dir:
            next_x = cur_x + x
            next_y = cur_y + y
            if s[next_y][next_x] == ".":
                while s[next_y][next_x] != "#":
                    passed.add((next_y, next_x))
                    next_x += x
                    next_y += y
                next_x -= x
                next_y -= y
                if (next_y, next_x) not in visited:
                    q.append((next_y, next_x))
                    visited.add((next_y, next_x))
    print(len(passed))


if __name__ == "__main__":
    main()
