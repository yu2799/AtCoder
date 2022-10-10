from sys import stdin


def f(x):
    return x**2 + 2 * x + 3


def main():
    input = stdin.readline
    t = int(input())
    print(f(f(f(t) + t) + f(f(t))))


if __name__ == "__main__":
    main()
