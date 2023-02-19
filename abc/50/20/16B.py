from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    res = "!"
    if a + b == c and a - b == c:
        res = "?"
    elif a + b == c:
        res = "+"
    elif a - b == c:
        res = "-"
    print(res)


if __name__ == "__main__":
    main()
