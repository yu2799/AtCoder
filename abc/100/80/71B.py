from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    d = [False] * 26
    for i in s:
        d[ord(i) - 97] = True
    for idx, i in enumerate(d):
        if not i:
            print(chr(idx + 97))
            return
    else:
        print("None")


if __name__ == '__main__':
    main()
