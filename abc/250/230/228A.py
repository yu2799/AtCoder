from sys import stdin


def main():
    input = stdin.readline
    s, t, x = map(int, input().split())
    if s < t:
        if s <= x < t:
            print("Yes")
        else:
            print("No")
    else:
        if x < t or s <= x:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()
