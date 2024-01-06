N = int(input())
arr = []
result = []
length = 0

for i in range(N//2, N + 1):
    arr = []
    arr.append(N)
    arr.append(i)
    num = i
    while True:
        second = arr[len(arr) - 1]
        first = arr[len(arr) - 2]
        num = first - second
        if num < 0: break
        arr.append(num)
        first = second
        second = num
        if len(arr) > length:
            length = len(arr)
            result = arr
            

print(length)
print(*result)