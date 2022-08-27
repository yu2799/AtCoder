from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(s[len(s) // 2])


if __name__ == "__main__":
    main()
