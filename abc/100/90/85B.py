from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = [int(input()) for _ in [0] * n]
    print(len(set(d)))


if __name__ == "__main__":
    main()
