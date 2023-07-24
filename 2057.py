from math import factorial
N = int(input())
check = [0 for _ in range(21)]
check[20] = 1
k = 19
fac = factorial(19)
if N != 0:
    while True:
        while True:
            k = check.index(1) - 1
            fac = factorial(k)
            check[k] = 1
            if N >= fac:
                break
        N -= fac
        if check[0] == 1 or N == 0:
            break
    if N == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')