from sys import stdin


def main():
    input = stdin.readline
    d = int(input())
    print("Christmas" + " Eve" * (25 - d))


if __name__ == "__main__":
    main()
