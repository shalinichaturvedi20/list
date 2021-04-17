# submission_type:
 
num=[50,40,23,35,33,70,56,12,5,10,7]
count=0
i=0
list1=[]
l=len(num)
while i<l:
    b=num[i]
    if b>20 and b<40:
        list1.append(num[i])
        count+=1
    i=i+1
print(count)
print(list1) 






