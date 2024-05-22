import random
num=random.randint(1,100)
# print(num)
turn=1
while turn:
    choice=int(input("Enter any number: "))
    if choice-num >0 and choice-num>=25:
        print("Too High")
    elif choice-num >0 and 0<choice-num<25:
        print("High")
    elif choice-num <0 and choice-num>-25:
        print("Low")                                                
    elif choice-num <0 and choice-num<-25:
        print("Too Low")
    else:
        print("Correct")
        break
    turn+=1