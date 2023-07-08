from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    c = list(map(int, input().split()))
    for i in range(n):
        if a + b == c[i]:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
