from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    w = input().split()
    tmp = set(["and", "not", "that", "the", "you"])
    for i in w:
        if i in tmp:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
