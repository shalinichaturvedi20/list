n=[50,40,23,70,56,12,5,10,7]
i=0
max=n[i]
while i<len(n):
    if max<n[i]:
        max=n[i]
    i=i+1
n.remove(max)
j=0
max=n[j]
while j<len(n):
    if max<n[j]:
        max=n[j]
    j=j+1
print(max)    




