from sys import stdin


def main():
    input = stdin.readline
    x1, y1, x2, y2 = map(int, input().split())
    p1 = []
    p2 = []
    dist = [
        [2, 1],
        [1, 2],
        [-1, 2],
        [-2, 1],
        [-2, -1],
        [-1, -2],
        [1, -2],
        [2, -1],
    ]
    for i in dist:
        p1.append([x1 + i[0], y1 + i[1]])
        p2.append([x2 + i[0], y2 + i[1]])
    for i in p1:
        for j in p2:
            if i == j:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
