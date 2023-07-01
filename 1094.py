X = int(input())
stick = 64
save = []
save.append(64)
tmp = 0
while sum(save) != X:
    if sum(save) > X:
        tmp = min(save) // 2
        save.append(tmp)
        save.remove(stick)
        if sum(save) < X:
            save.append(tmp)
    stick = tmp
print(len(save))  