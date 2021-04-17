a=[1,0,0,1,1,0,1,1]
i=1
s=0
k=0
while i<=len(a):
    b=(2**k)
    c=b*a[-i]
    s=s+c
    i=i+1
    k=k+1
print(s)    