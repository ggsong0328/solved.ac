N = int(input())
words = []
ans = []
for _ in range(N):
    word = input()
    words.append(word)

ans = list(set(words))
ans.sort()
ans.sort(key = len)
    
for word in ans:
    print(word)