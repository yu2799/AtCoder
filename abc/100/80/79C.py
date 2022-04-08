s = input()
for i in range(8):
    res = s[0]
    for j in range(3):
        if i >> j & 1:
            res += "+"
        else:
            res += "-"
        res += s[j+1]
    if eval(res) == 7:
        print(res + "=7")
        exit()
