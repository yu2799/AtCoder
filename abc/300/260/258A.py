from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    h = 21 + k // 60
    m = k % 60
    print(f"{h}:{m:02}")


if __name__ == "__main__":
    main()
