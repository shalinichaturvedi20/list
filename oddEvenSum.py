elements=[23,14,56,12,19,9,15,25,31,42,43]
i=0
s=0
s1=0
c=0
c1=0
while i<len(elements):
    if elements[i]%2==0:
        s=s+(elements[i])
        c=c+1
    else:
        s1=s1+(elements[i])
        c1=c1+1
    i=i+1
sum=s+s1
count=c+c1
print(s,c,"even")
print(s1,c1,"odd")
print(sum,count)            