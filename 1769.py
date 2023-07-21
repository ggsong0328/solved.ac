X = input()
cnt = 0
while int(X) // 10 != 0:
    sum = 0
    for i in range(len(X)):
        sum += int(X[i])
    X = str(sum)
    cnt += 1

print(cnt)
if int(X) % 3 == 0:
    print('YES')
else:
    print('NO')