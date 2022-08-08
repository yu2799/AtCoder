from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [list(input()[:-1]) for _ in [0] * h]
    row = set()
    col = set()
    for i in range(h):
        if a[i].count("#") == 0:
            row.add(i)

    for i in range(w):
        for j in range(h):
            if a[j][i] == "#":
                break
        else:
            col.add(i)

    for i in range(h):
        tmp = ""
        if i in row:
            continue
        for j in range(w):
            if j not in col:
                tmp += a[i][j]
        print(tmp)


if __name__ == "__main__":
    main()
