s = input()[::-1]
l = len(s)
now = 0
while now < l:
    if s[now:now+5] == "maerd" or s[now:now+5] == "esare":
        now += 5
    elif s[now:now+6] == "resare":
        now += 6
    elif s[now:now+7] == "remaerd":
        now += 7
    else:
        print("NO")
        exit()

print("YES")
