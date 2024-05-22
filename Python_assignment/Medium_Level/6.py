num=int(input("Number: "))
def func(num):
    flag=0
    if (num%2==0):
        num=num/2
    else :
        flag=1
    if (flag==0 and num>0):
        func(num)
    elif (num==1):
         print("Yes")
    else :
       print("No")
func(num)