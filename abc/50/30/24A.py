from sys import stdin


def main():
    input = stdin.readline
    a, b, c, k = map(int, input().split())
    s, t = map(int, input().split())
    print(a * s + b * t - ((s + t) * c if k <= s + t else 0))


if __name__ == "__main__":
    main()
