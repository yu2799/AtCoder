from sys import stdin


def main():
    input = stdin.readline
    c = list(input()[:-1])
    print("Won" if len(set(c)) == 1 else "Lost")


if __name__ == "__main__":
    main()
