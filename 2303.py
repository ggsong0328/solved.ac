from itertools import combinations

N = int(input())
card = []
for i in range(N):
    ppl = list(map(int, input().split()))
    card.append(ppl)

idx = 0
maximum = 0

for i in range(N):
    arr = list(combinations(card[i], 3))
    for j in range(len(arr)):
        arr[j] = sum(arr[j]) % 10
    if maximum <= max(arr):
        maximum = max(arr)
        idx = i + 1

print(idx)