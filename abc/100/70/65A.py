from sys import stdin


def main():
    input = stdin.readline
    x, a, b = map(int, input().split())
    print("delicious" if b <= a else ("safe" if b <= a + x else "dangerous"))


if __name__ == "__main__":
    main()
