from sys import stdin


def main():
    input = stdin.readline
    print(len(set(map(int, input().split()))))


if __name__ == "__main__":
    main()
