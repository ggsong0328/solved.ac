import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, C, M = list(sys.stdin.readline().split())
    message = [[0 for _ in range(int(C))] for _ in range(int(R))]
    for i in range(len(M)):
        message[i//int(C)][i%int(C)] = int(M[i])

    #print(message)

    result = []
    rows, cols = len(message), len(message[0])
    left, right, top, bottom = 0, cols-1, 0, rows-1

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(message[top][col])

        for row in range(top + 1, bottom + 1):
            result.append(message[row][right])

        if top < bottom:
            for col in range(right - 1, left - 1, -1):
                result.append(message[bottom][col])

        if left < right:
            for row in range(bottom - 1, top, -1):
                result.append(message[row][left])

        left += 1
        right -= 1
        top += 1
        bottom -= 1
        
    arr = [result[i:i + 5] for i in range(0, len(result), 5)]

    ans = []
    for row in arr:
        row_str = [str(item) for item in row]
        if len(row_str) == 5:
            tmp = ''.join(row_str)
            ans.append(tmp)

    while ans[0] == '00000':
        del ans[0]

    while ans[-1] == '00000':
        del ans[-1]    

    #print(ans)

    alpha_result = []

    for dec in ans:
        if dec == '00000':
            alpha_result.append(' ')
        else:
            decimal_value = int(dec, 2) - 1
            if 0 <= decimal_value < 26:
                alpha_result.append(chr(decimal_value + ord('A')))


    for alpha in alpha_result:
        print(alpha, end='')
