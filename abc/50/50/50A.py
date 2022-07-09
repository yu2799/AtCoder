from sys import stdin


def main():
    input = stdin.readline
    a, op, b = input().split()
    print(int(a) + int(b) if op == "+" else int(a) - int(b))


if __name__ == "__main__":
    main()
