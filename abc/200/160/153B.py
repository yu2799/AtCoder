from sys import stdin


def main():
    input = stdin.readline
    h, _ = map(int, input().split())
    a = list(map(int, input().split()))
    print("Yes" if h <= sum(a) else "No")


if __name__ == "__main__":
    main()
