from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    print(
        "Possible"
        if a % 3 == 0 or b % 3 == 0 or (a + b) % 3 == 0
        else "Impossible"
    )


if __name__ == "__main__":
    main()
