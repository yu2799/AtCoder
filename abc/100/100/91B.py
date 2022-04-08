def main():
    n = int(input())
    s = [input() for _ in range(n)]
    m = int(input())
    t = [input() for _ in range(m)]

    res = 0
    for i in s:
        tmp = 0
        for j in s:
            if i == j:
                tmp += 1
        for k in t:
            if i == k:
                tmp -= 1
        if res < tmp:
            res = tmp

    print(res)


if __name__ == '__main__':
    main()
