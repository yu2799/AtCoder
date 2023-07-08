from sys import stdin


def main():
    input = stdin.readline
    s = list(map(int, input().split()))
    prev = 0
    for i in s:
        if i < prev or i < 100 or 675 < i or i % 25 != 0:
            print("No")
            return
        prev = i
    print("Yes")


if __name__ == "__main__":
    main()
