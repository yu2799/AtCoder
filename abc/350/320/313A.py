from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    p = list(map(int, input().split()))
    if p[0] == max(p):
        if n == 1 or p[0] != max(p[1:]):
            print(0)
        else:
            print(1)
    else:
        print(max(p) - p[0] + 1)


if __name__ == "__main__":
    main()
