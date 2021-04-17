a=[1,2,3,4,5,6]
b=[2,3,1,0,6,7]
i=0
z=[]
while i<len(a):
    c=a[i]
    if c not in b:
        z.append(c)
    i=i+1
print(z)        