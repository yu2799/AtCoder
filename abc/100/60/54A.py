from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    if a == b:
        print("Draw")
    elif a == 1 or (a > b and b != 1):
        print("Alice")
    else:
        print("Bob")


if __name__ == "__main__":
    main()
