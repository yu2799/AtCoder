from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    for c in range(b, 0, -1):
        if (a + c - 1) // c < b // c:
            print(c)
            return


if __name__ == "__main__":
    main()
