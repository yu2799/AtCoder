from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n >= 42:
        n += 1
    print(f"AGC{n:03}")


if __name__ == "__main__":
    main()
