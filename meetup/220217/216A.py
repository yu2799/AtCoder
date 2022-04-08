from sys import stdin


def main():
    input = stdin.readline
    x, y = input().split(".")
    if int(y) <= 2:
        print(f"{x}-")
    elif int(y) <= 6:
        print(f"{x}")
    else:
        print(f"{x}+")


if __name__ == "__main__":
    main()
