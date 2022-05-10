from sys import stdin


def main():
    input = stdin.readline
    n, a, b = map(int, input().split())
    for i in range(n):
        res = ""
        for j in range(n):
            if not i % 2:
                if not j % 2:
                    res += "." * b
                else:
                    res += "#" * b
            else:
                if j % 2:
                    res += "." * b
                else:
                    res += "#" * b
        for j in range(a):
            print(res)


if __name__ == '__main__':
    main()
