from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    a = list(set(map(int, input().split())))
    print("Yes" if len(a) == 1 else "No")


if __name__ == "__main__":
    main()
