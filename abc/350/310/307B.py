from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = [input()[:-1] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            buf = s[i] + s[j]
            if buf == buf[::-1]:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
