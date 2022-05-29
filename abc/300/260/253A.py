from sys import stdin


def main():
    input = stdin.readline
    a, b, c = map(int, input().split())
    tmp = [a, b, c]
    tmp.sort()
    print("Yes" if tmp[1] == b else "No")


if __name__ == "__main__":
    main()
