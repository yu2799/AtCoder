from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    h = list(map(int, input().split()))
    prev = h[0]
    for i in h[1:]:
        if prev >= i:
            break
        prev = i
    print(prev)


if __name__ == "__main__":
    main()
