from sys import stdin


def main():
    input = stdin.readline
    s = input()[:-1]
    n = len(s)
    print(
        "Yes"
        if (
            s == s[::-1]
            and s[: (n - 1) // 2] == s[: (n - 1) // 2][::-1]
            and s[(n + 3) // 2 - 1 :] == s[(n + 3) // 2 - 1 :][::-1]
        )
        else "No"
    )


if __name__ == "__main__":
    main()
