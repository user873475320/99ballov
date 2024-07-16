arr = []
for i in 'SKUF':
    for j in 'SKUF':
        for k in 'SKUF':
            for l in 'SKUF':
                arr.append(i + j + k + l)

resArr = []
for word in arr:
    strR = ""
    for i in range(len(word)):
        tmpR = bin(ord(word[i]))[2:]
        tmpR = tmpR + str(sum(int(j) for j in bin(ord(word[3]))[2:]) % 2)
        tmpR = '1' + tmpR if bin(ord(word[0]))[2:].count('0') % 2 == 1 else tmpR

        strR += tmpR

    r = strR.count('1')
    if r > 10:
        resArr.append(r)

print(min(resArr)) # 13
