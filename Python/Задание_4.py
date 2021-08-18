s = input()
j = len(s)
count=1
for i in range(j):
    a = s[i]
    if i==j-1:
        print(a,end='')
        print(count,end='')
        break
    if s[i]==s[i+1]:
        count+=1
    else:
        print(a,end='')
        print(count,end='')
        count=1