from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    d = set()
    w = input()[:-1]
    d.add(w)
    prev = w[-1]
    for _ in [0] * (n - 1):
        w = input()[:-1]
        if w in d or prev != w[0]:
            print("No")
            return
        d.add(w)
        prev = w[-1]
    print("Yes")


if __name__ == "__main__":
    main()
