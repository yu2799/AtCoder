from sys import stdin


def main():
    input = stdin.readline
    n, m, h, k = map(int, input().split())
    s = input()[:-1]
    xy = set(tuple(map(int, input().split())) for _ in range(m))
    cur_x = 0
    cur_y = 0
    for i in s:
        if i == "R":
            cur_x += 1
        if i == "L":
            cur_x -= 1
        if i == "U":
            cur_y += 1
        if i == "D":
            cur_y -= 1
        h -= 1
        if h < 0:
            print("No")
            return
        if (cur_x, cur_y) in xy and h < k:
            h = k
            xy.remove((cur_x, cur_y))
    print("Yes")


if __name__ == "__main__":
    main()
