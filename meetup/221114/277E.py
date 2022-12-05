from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    g = [[] for _ in [0] * n]
    for _ in [0] * n:
        a, b = map(int, input().split())


if __name__ == "__main__":
    main()
