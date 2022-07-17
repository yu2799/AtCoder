from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    if n[0] == n[1] == n[2] or n[1] == n[2] == n[3]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
