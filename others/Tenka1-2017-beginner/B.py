from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    ab = [tuple(map(int, input().split())) for _ in [0] * n]
    ab.sort(reverse=True)
    print(sum(ab[0]))


if __name__ == "__main__":
    main()
