from sys import stdin


def main():
    input = stdin.readline
    _, k = map(int, input().split())
    a = list(sorted(map(int, input().split()), reverse=True))
    print(sum(a[:k]))


if __name__ == "__main__":
    main()
