from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    print("ABC" if n < 1000 else "ABD")


if __name__ == "__main__":
    main()
