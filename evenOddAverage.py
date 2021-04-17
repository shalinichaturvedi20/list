elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
e=[]
o=[]
s=0
s1=0
a=0
a1=0
while i<len(elements):
    if elements[i]%2==0:
        e.append(elements[i])
        s=s+(elements[i])
        a=s/len(elements)
    else:
        o.append(elements[i])
        s1=s1+(elements[i])
        a1=s/len(elements)
    i=i+1
print(a,"even")
print(a1,"odd")           