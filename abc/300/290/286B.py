from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    print(s.replace("na", "nya"))


if __name__ == "__main__":
    main()
