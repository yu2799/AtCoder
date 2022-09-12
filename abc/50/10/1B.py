from sys import stdin


def main():
    input = stdin.readline
    m = int(input())
    if m < 100:
        print("00")
    elif m <= 5000:
        print(f"{m//100:02}")
    elif 6000 <= m <= 30000:
        print(m // 1000 + 50)
    elif 35000 <= m <= 70000:
        print((m // 1000 - 30) // 5 + 80)
    else:
        print(89)


if __name__ == "__main__":
    main()
