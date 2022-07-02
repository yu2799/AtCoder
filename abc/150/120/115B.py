from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = [int(input()) for _ in [0] * n]
    print(sum(p) - max(p) // 2)


if __name__ == "__main__":
    main()
