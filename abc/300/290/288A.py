from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    res = []
    for _ in range(n):
        a, b = map(int, input().split())
        res.append(a + b)
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
