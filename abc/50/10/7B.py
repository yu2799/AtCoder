from sys import stdin


def main():
    input = stdin.readline
    a = input()[:-1]
    if a == "a":
        print(-1)
    else:
        print("a")


if __name__ == "__main__":
    main()
