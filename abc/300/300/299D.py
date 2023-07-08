left = 1
right = int(input())
while abs(left - right) > 1:
    mid = (left + right) // 2
    print(f"? {mid}")
    tmp = int(input())
    if tmp == 0:
        left = mid
    else:
        right = mid
print(f"! {left}")
