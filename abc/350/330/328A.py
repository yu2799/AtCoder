from sys import stdin


def main():
    input = stdin.readline
    n, x = map(int, input().split())
    s = list(map(int, input().split()))
    print(sum(i for i in s if i <= x))


if __name__ == "__main__":
    main()
