from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    for h in range(1, 3501):
        for w in range(1, 3501):
            if (
                4 * h * w - n * w - n * h > 0
                and (n * h * w) % (4 * h * w - n * w - n * h) == 0
            ):
                print(h, (n * h * w) // (4 * h * w - n * w - n * h), w)
                return


if __name__ == "__main__":
    main()
