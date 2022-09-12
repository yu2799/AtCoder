from collections import Counter
from sys import stdin


def main():
    input = stdin.readline
    s = Counter(list(input()[:-1]))
    print(s["1"])


if __name__ == "__main__":
    main()
