from sys import stdin


def main():
    input = stdin.readline
    _, x = map(int, input().split())
    a = set(map(int, input().split()))
    b = set([i + x for i in a])
    for i in a:
        if i in b:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
