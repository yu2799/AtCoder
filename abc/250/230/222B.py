from sys import stdin


def main():
    input = stdin.readline
    _, p = map(int, input().split())
    a = list(map(int, input().split()))
    print(len([i for i in a if i < p]))


if __name__ == "__main__":
    main()
