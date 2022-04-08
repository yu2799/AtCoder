from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in [0] * h]
    b = [[int(i) for i in input().split()] for _ in [0] * h]
    res = 0
    for i in range(h-1):
        for j in range(w-1):
            diff = b[i][j] - a[i][j]
            a[i][j] += diff
            a[i][j+1] += diff
            a[i+1][j] += diff
            a[i+1][j+1] += diff
            res += abs(diff)

    for i in range(h):
        for j in range(w):
            if a[i][j] != b[i][j]:
                print("No")
                exit()
    else:
        print("Yes")
        print(res)


if __name__ == '__main__':
    main()
