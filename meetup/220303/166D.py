from sys import stdin


def main():
    input = stdin.readline
    x = int(input())
    for b in range(-120, 120):
        for a in range(b, 120):
            tmp = a ** 5 - b ** 5
            if tmp == x:
                print(a, b)
                return
            elif tmp > x:
                break


if __name__ == "__main__":
    main()
