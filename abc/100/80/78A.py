from sys import stdin


def main():
    input = stdin.readline
    x, y = input().split()
    print("<" if x < y else (">" if x > y else "="))


if __name__ == "__main__":
    main()
