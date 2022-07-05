from sys import stdin


def func(x):
    return x**2 + 2 * x + 3


def main():
    input = stdin.readline
    t = int(input())
    print(func(func(func(t) + t) + func(func(t))))


if __name__ == "__main__":
    main()
