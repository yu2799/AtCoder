from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    t = input()[:-1]
    res = [0, 0]
    dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    pos = 0
    for i in t:
        if i == "S":
            res[0] += dir[pos][0]
            res[1] += dir[pos][1]
        else:
            pos += 1
            pos %= 4
    print(*res)


if __name__ == "__main__":
    main()
