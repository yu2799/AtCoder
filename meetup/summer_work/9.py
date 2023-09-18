from sys import stdin


def main():
    input = stdin.readline
    n, m = map(int, input().split())
    a = [input()[:-1] for _ in range(2 * n)]
    d = [[0, i] for i in range(2 * n)]
    for i in range(m):
        for j in range(n):
            left = a[d[2 * j][1]][i]
            right = a[d[2 * j + 1][1]][i]
            if (
                (left == "G" and right == "C")
                or (left == "C" and right == "P")
                or (left == "P" and right == "G")
            ):
                d[2 * j][0] -= 1
            elif (
                (right == "G" and left == "C")
                or (right == "C" and left == "P")
                or (right == "P" and left == "G")
            ):
                d[2 * j + 1][0] -= 1
        d.sort()
    for _, i in d:
        print(i + 1)


if __name__ == "__main__":
    main()
