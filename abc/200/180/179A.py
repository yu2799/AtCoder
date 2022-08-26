from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    s += "es" if s[-1] == "s" else "s"
    print(s)


if __name__ == "__main__":
    main()
