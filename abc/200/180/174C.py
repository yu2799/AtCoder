from sys import stdin


def main():
    input = stdin.readline
    k = int(input())
    if k % 2 != 0 or k % 5 == 0:
        num = 0
        tmp = set()
        for i in range(1, k + 1):
            num = (num * 10 + 7) % k
            if num == 0:
                print(i)
                return
            if num in tmp:
                break
            tmp.add(num)
    print(-1)


if __name__ == "__main__":
    main()
