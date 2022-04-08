s = input()
o = s.count("o")
x = s.count("x")
q = len(s) - o - x
if o == 0:
    print(q ** 4)
elif o == 1:
    print(4 * q ** 3 + 6 * q ** 2 + 4 * q + 1)
elif o == 3:
    print(24 * q + 12 * 3)
elif o == 4:
    print(24)
elif o >= 5:
    print(0)
