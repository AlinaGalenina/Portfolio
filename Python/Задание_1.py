list = []
n = int(input())
m=1
for i in range (n):
    list.insert(i, i+1)
list2= [[list[i] for j in range (m+i)] for i in range(n)]
x = [] # создаем
for i in range(len(list2)):
    for j in range(len (list2[i])):
        x.append(list2[i][j]) 
for i in range (n):
    print(x[i],end=' ')