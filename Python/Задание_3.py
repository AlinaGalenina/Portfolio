s=0
a = [int(i) for i in input().split()]
l=len(a)
if l==1:
    print (a[0])
else:
    for i in range(l):
        if i==0:
            s=a[i+1]+a[l-1]
            print (s,end='\t')
        else:
            if i==l-1:
                s=a[i-1]+a[0]
                print (s,end='\t')
            else:
                s=a[i+1]+a[i-1]
                print (s,end='\t')