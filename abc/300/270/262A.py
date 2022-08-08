from sys import stdin


def main():
    input = stdin.readline
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            return
        y += 1


if __name__ == "__main__":
    main()
