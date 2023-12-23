from sys import stdin


def main():
    input = stdin.readline
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(True for i in a if l <= i))


if __name__ == "__main__":
    main()
