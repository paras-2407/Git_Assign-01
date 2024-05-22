num=int(input("Number: "))
# num=list(num)
i=num
revnum=[]
while i/10!=0:
    revnum.append(i%10)
    i//=10
for i in revnum:
    print(i, end="")