from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    a = list(set(map(int, input().split())))
    a.sort()
    print(a[-2])


if __name__ == "__main__":
    main()
