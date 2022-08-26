from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    for _ in [0] * n:
        a = int(input())
        if a % 2 != 0:
            print("first")
            return
    print("second")


if __name__ == "__main__":
    main()
