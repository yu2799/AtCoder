from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(len(s) // 2 - s.count("p"))


if __name__ == "__main__":
    main()
