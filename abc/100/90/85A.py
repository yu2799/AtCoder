from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    print(f"2018{s[4:]}")


if __name__ == "__main__":
    main()
