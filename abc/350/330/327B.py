from sys import stdin


def main():
    input = stdin.readline
    b = int(input())
    a = 1
    while pow(a, a) < b:
        a += 1
    print(a if pow(a, a) == b else -1)


if __name__ == "__main__":
    main()
