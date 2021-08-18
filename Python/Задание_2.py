A = []
row = input()
s=0
while (row != "end"):
    str=row.split()
    for i in range(len(str)):
        str[i] = int(str[i])
    A.append(str)
    row = input()
n = len(A)
m = len(A[0])
if n==1 and m==1:
    s+=A[0][0]*4
    print(s)
else:
    B = [[] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            s=0
            k=A[i-1][j]+A[i][j-1]+A[i-n+1][j]+A[i][j-m+1]
            s+=k
            B[i].insert(j, s)
    for i in range(len(B)):
        for j in range(len(B[i])):
            print(B[i][j], end = ' ')
        print()