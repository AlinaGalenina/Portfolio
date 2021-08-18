with open('input.txt') as inf:
    s = inf.readline()

j = len(s)
w = ''
for i in range(j):
    if i==j-1:
         w = w + a*int(s[i])
    else:
        if s[i].isalpha():
            a = s[i]
        else:
            if s[i+1].isdigit():
                w = w + a*int(s[i]+s[i+1])
            else:
                if s[i-1].isalpha():
                    w = w + a*int(s[i])

with open('output.txt', 'w') as ouf:
    ouf.write(w)