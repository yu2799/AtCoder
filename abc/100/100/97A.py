from sys import stdin


def main():
    input = stdin.readline
    a, b, c, d = map(int, input().split())
    print(
        "Yes"
        if (abs(a - b) <= d and abs(b - c) <= d) or abs(a - c) <= d
        else "No"
    )


if __name__ == "__main__":
    main()
