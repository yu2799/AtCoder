from sys import stdin


def main():
    input = stdin.readline
    _ = int(input())
    s = input()[:-1]
    res = 0
    tmp = 0
    for i in s:
        if i == "I":
            tmp += 1
            if res < tmp:
                res = tmp
        else:
            tmp -= 1
    print(res)


if __name__ == "__main__":
    main()
