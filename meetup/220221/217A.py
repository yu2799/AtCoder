from sys import stdin


def main():
    input = stdin.readline
    s, t = input().split()
    res = sorted([s, t])
    print("Yes" if res[0] == s else "No")


if __name__ == "__main__":
    main()
