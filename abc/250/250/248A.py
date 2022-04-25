from sys import stdin


def main():
    input = stdin.readline
    s = list(input()[:-1])
    buf = [str(i) for i in range(10)]
    for i in buf:
        if i not in s:
            print(i)
            return


if __name__ == '__main__':
    main()
