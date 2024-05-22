lst=[]

num=int(input("Enter lenght of list"))

for i in range(0,num):
    e=int(input())
    lst.append(e)

d={i:lst.count(i) for i in lst}

print(d)