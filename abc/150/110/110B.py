from sys import stdin


def main():
    input = stdin.readline
    _, _, X, Y = map(int, input().split())
    x = list(sorted(map(int, input().split())))
    y = list(sorted(map(int, input().split())))
    print(
        "No War" if x[-1] < y[0] and X < x[-1] < Y and X < y[0] < Y else "War"
    )


if __name__ == "__main__":
    main()
