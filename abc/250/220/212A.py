from sys import stdin


def main():
    input = stdin.readline
    a, b = map(int, input().split())
    if a == 0:
        print("Silver")
    elif b == 0:
        print("Gold")
    else:
        print("Alloy")

if __name__ == '__main__':
    main()