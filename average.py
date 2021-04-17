num=[23,14,56,12,1,9,15,25,31,42,143]
sum=0
sum1=0
i=0
while i<len(num):
    if num[i]%2==0:
        sum+=num[i]
    else:
        sum1+=num[i]
    i=i+1
print(sum/len(num),"average value of even number")
print(sum1/len(num),"average value of odd number")


