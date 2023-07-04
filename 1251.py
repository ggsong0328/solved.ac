word = input()
ans = []
for i in range(1, len(word)-1):
    for j in range(i + 1, len(word)):
        str1 = word[:i]
        str2 = word[i:j]
        str3 = word[j:]
        ans.append("".join(reversed(str1))+"".join(reversed(str2))+"".join(reversed(str3)))

print(min(ans))