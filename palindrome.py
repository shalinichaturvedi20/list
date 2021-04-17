t="naman"
a=list(t)
b=[]
i=1
while i<=len(t):
    print(a[-i])
    b.append(a[-i])
    i+=1
if b==a:
    print("palindrome")
else:
    print("not palindrome")        





