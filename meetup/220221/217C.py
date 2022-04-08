from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [0] * n
    for i, j in enumerate(p):
        q[j - 1] = i + 1
    print(*q)


if __name__ == "__main__":
    main()
