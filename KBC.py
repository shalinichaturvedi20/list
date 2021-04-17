print("welcom to KBC")
print("kon banega krorpati")
question_list=["how many continents are there",
              "what is the capital of India",
               "NG me kaun kaun sa cource padhaya jata hai"]
option_list=[["1.Four","2.Nine","3.Seven","4.Eight"],
            ["1.chandigarh","2.bhopal","3.chennai","4.delahi"],
            ["1.software engineering","2.counseling","3.Tourism","Agriculture"]]
solution=[3, 4, 1]
answer=["3.seven","4.eight","3.chennai","4.delhi","1.software engineering","3.tourism"]
i=0
amount=1000
count=0
b=0
a=1
while i<len(question_list):
    print(question_list[i])
    j=0
    k=1
    while j<len(option_list[i]):
        print(option_list[i][j])
        j=j+1
    lifeline=input("do you want lifeline")
    if lifeline=="yes":
        print("5050")
        if count==0:
            print(answer[b+i])
            print(answer[b+a])
            num=int(input("enter the answer"))
            if num==solution[i]:
                print("your answer is right")
                print("you won",amount,"$")
            else:
                print("answer is wrong")
                print("you loose the game")
                break
            count=count+1
            print()
        else:
            print("you had already used lifeline")
            e=int(input("enter the answer"))
            if e==solution[i]:
                print("your answer is right")
                print("you won",amount,"$")
            else:
                print("answer is wrong")
                print("you loose the game")
                break
            print()  
    else:
        f=int(input("enter the answer"))
        if f==solution[i]:
            print("your answer is right")
            print("you won",amount,"$")
        else:
            print("your answer is wrong")
            print("you loose the game")
            break
        print()
    amount=amount+10000    
    i=i+1 
    a=a+1
    b=b+1
print("you won",amount,"$")
print("thanku for playing")    
    