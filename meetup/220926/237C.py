from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    if len(set(s)) == 1:
        print("Yes")
        return
    left = 0
    right = len(s) - 1
    while s[right] == "a":
        right -= 1
        if s[left] == "a":
            left += 1

    while left <= right:
        if s[left] != s[right]:
            print("No")
            return
        left += 1
        right -= 1
    print("Yes")


if __name__ == "__main__":
    main()
