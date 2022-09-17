from sys import stdin


def main():
    input = stdin.readline
    s = [input()[:-1] for _ in [0] * 10]
    flag = False
    b = 10
    d = 10
    for i in range(10):
        tmp = s[i].find("#")
        if tmp != -1:
            c = tmp + 1
            d = s[i].count("#") + tmp
            if not flag:
                a = i + 1
                flag = True
        elif flag:
            b = i
            break
    print(a, b)
    print(c, d)


if __name__ == "__main__":
    main()
