def  modify_list(l : list):
    t=len(l)
    for i in range(t-1,-1,-1):
        if l[i]%2 ==0:
            l[i]=int(l[i]/2)
        else:
            del l[i]