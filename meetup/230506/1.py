from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [input()[:-1] for _ in range(n)]
    print("Yes" if len([1 for i in s if i == "For"]) * 2 > n else "No")


if __name__ == "__main__":
    main()
