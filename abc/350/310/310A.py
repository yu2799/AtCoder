from sys import stdin


def main():
    input = stdin.readline
    n, p, q = map(int, input().split())
    d = list(map(int, input().split()))
    print(min(p, q + min(d)))


if __name__ == "__main__":
    main()
