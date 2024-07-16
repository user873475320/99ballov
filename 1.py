arr = []
for i in range(1, 1000000):
    r = bin(i)[2:]
    ch1 = sum(i for i in range(len(r)) if r[i] == '1') % 2
    ch2 = sum(i for i in range(len(r)) if r[i] == '0') % 2

    r = str(ch1) + r + str(ch2)

    if int(r, 2) > 81:
        arr.append(int(r, 2))


print(oct(min(arr))[2:]) # 125
