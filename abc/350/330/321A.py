from sys import stdin


def main():
    input = stdin.readline
    n = input()[:-1]
    l = len(n)
    prev = int(n[0])
    for i in range(1, l):
        if int(prev) <= int(n[i]):
            print("No")
            return
        prev = n[i]
    print("Yes")


if __name__ == "__main__":
    main()
