from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    flag = [False] * 26
    for i in s:
        flag[ord(i) - 97] = True
    for i in range(26):
        if not flag[i]:
            print(chr(i + 97))
            return
    print("None")


if __name__ == "__main__":
    main()
