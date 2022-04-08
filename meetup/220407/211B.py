from sys import stdin


def main():
    input = stdin.readline
    s = [input()[:-1] for _ in [0] * 4]
    l = len(set(s))
    print("Yes" if l == 4 else "No")


if __name__ == "__main__":
    main()
