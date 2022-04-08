from sys import stdin


def main():
    input = stdin.readline
    h, w = map(int, input().split())
    a = [[int(i) for i in input().split()] for _ in [0] * h]
    for i in range(w):
        tmp = []
        for j in range(h):
            tmp.append(a[j][i])
        print(*tmp, sep=" ")


if __name__ == "__main__":
    main()
