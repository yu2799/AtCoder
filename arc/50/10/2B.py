from datetime import date, timedelta
from sys import stdin


def main():
    input = stdin.readline
    y, m, d = map(int, input().split("/"))
    td = timedelta(days=1)

    now = date(y, m, d)
    while not (now.year / now.month / now.day).is_integer():
        now = now + td
    print(now.strftime("%Y/%m/%d"))


if __name__ == "__main__":
    main()
