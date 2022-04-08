from sys import stdin


def main():
    input = stdin.readline
    n = int(input())
    if n % 2 == 0:
        for i in range(2**n, 2**(n-1)-1, -2):
            cnt = 0
            buf = []

            tmp = bin(i)[2:]
            for j in tmp:
                if j == "1":
                    cnt += 1
                    buf.append("(")
                else:
                    cnt -= 1
                    buf.append(")")
                if cnt < 0:
                    break
            if cnt == 0 and len(buf) == n:
                print(*buf, sep="")


if __name__ == '__main__':
    main()
