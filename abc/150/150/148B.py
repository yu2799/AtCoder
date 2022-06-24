from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s, t = input().split()
    for i, j in zip(s, t):
        print(i, j, sep="", end="")


if __name__ == "__main__":
    main()
