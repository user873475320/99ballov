arr = []
for i in range(1, 1000000):
    r = bin(i)[2:]

    if len(r) % 3 != 0:
        newR = r + '0' * (3 - len(r) % 3)
    else:
        newR = r

    count_odd_triad = 0
    count_even_triad = 0
    for j in range(0, len(newR), 3):
        if sum(int(newR[k]) for k in range(j, j + 3)) % 2 == 1:
            count_odd_triad += 1
        else:
            count_even_triad += 1

    r = r + str(count_odd_triad % 2) + str(count_even_triad % 2)

    if int(r, 2) > 80:
        arr.append(int(r, 2))

print(oct(min(arr))[2:]) # 127
