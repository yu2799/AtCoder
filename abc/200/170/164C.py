from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [input()[:-1] for _ in [0] * n]
    print(len(set(s)))


if __name__ == "__main__":
    main()
