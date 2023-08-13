import sys
N = int(sys.stdin.readline())

max_arr = []

for i in range(N//2 + 1, N + 1):

    first = N
    second = i
    arr = [N, i]

    while True:
        next_num = first - second
        if next_num >= 0:
            arr.append(next_num)
            first = second
            second = next_num
        else:
            if len(arr) > len(max_arr):
                max_arr = arr
            break

print(len(max_arr))
print(*max_arr)
    