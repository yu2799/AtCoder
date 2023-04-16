from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    print("Yes" if "o" in s and "x" not in s else "No")


if __name__ == "__main__":
    main()
