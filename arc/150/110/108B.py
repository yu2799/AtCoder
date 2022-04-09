from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    s = input()[:-1]
    q = []
    for i in s:
        if i == "x" and len(q) > 1 and q[-1] == "o" and q[-2] == "f":
            q.pop()
            q.pop()
        else:
            q.append(i)
    print(len(q))


if __name__ == '__main__':
    main()
