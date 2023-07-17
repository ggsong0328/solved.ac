N = int(input())
factorial = 1

while N != 0:
    factorial *= N
    N -= 1

#print(factorial)

cnt = 0
while factorial % 10 == 0:
    factorial = factorial // 10
    cnt += 1

print(cnt)