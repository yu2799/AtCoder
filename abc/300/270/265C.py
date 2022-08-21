from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    g = [list(input()[:-1]) for _ in [0] * h]
    i = 0
    j = 0
    visited = set()
    while True:
        op = g[i][j]
        if op == "U":
            i -= 1
            if i == -1:
                print(i + 2, j + 1)
                return
        elif op == "D":
            i += 1
            if i == h:
                print(i, j + 1)
                return
        elif op == "L":
            j -= 1
            if j == -1:
                print(i + 1, j + 2)
                return
        else:
            j += 1
            if j == w:
                print(i + 1, j)
                return
        if (i, j) in visited:
            print(-1)
            return
        visited.add((i, j))


if __name__ == "__main__":
    main()
