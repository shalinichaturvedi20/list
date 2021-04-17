num=[40,50,70,20,60] 
i=0
a=num[i]
while i<len(num):
    b=num[i]
    if b>a:
        a=b
    i=i+1
print(a,"maximum")          
